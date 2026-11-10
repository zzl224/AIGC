async function generateVideo({ prompt, params }) {
    const content = [{ type: 'text', text: prompt }];
    images.forEach((url, index) => content.push({
        type: 'image_url',
        role: params.mode === 'reference' ? 'reference_image' : (index === 0 ? 'first_frame' : 'last_frame'),
        image_url: { url }
    }));
    // 创建视频生成任务
    const createResponse = await fetch(http.url(new URL('/v2/video_generation', baseUrl).href), {
        signal,
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + apiKey,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            model: 'MiniMax-H3-Max',
            content,
            duration: Math.min(15, Math.max(5, params.seconds || 6)),
            resolution: params.resolution === '1080p' ? '768P' : '480P',
            ...(images.length && params.mode === 'frames' ? {} : { ratio: params.ratio || '16:9' }),
            aigc_watermark: params.watermark || false
        })
    });

    if (!createResponse.ok) {
        const error = await createResponse.text();
        throw new Error('视频任务创建失败: ' + error);
    }

    const createData = await createResponse.json();
    const taskId = createData.task_id;

    if (!taskId) {
        throw new Error('未获取到任务ID');
    }

    // 轮询任务状态
    for (let i = 0; i < 120; i++) {
        await new Promise(resolve => setTimeout(resolve, 5000));

        const queryResponse = await fetch(http.url(new URL('/v2/query/video_generation/' + taskId, baseUrl).href), {
            signal,
            headers: {
                'Authorization': 'Bearer ' + apiKey
            }
        });

        if (!queryResponse.ok) {
            throw new Error('查询任务状态失败: ' + queryResponse.status);
        }

        const queryData = await queryResponse.json();
        const task = queryData.task;

        if (task.status === 'succeeded' && task.content?.url) {
            return task.content.url;
        } else if (task.status === 'failed') {
            throw new Error('视频生成失败: ' + (task.error?.message || '未知错误'));
        }
    }

    throw new Error('视频生成超时（10分钟）');
}

return await generateVideo({ prompt, params });
