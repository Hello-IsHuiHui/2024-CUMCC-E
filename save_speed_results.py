def save_results_to_csv(speeds, output_file='./问题2支撑材料/speed_analysis_results.csv'):
    results = []

    # 添加纬中路各路段速度
    for (start, end), speed in speeds['segment_speeds']['wei_zhong_road']:
        results.append({
            '道路': '纬中路',
            '起点': start,
            '终点': end, 
            '路段速度(km/h)': round(speed, 2)
        })

    # 添加经中路各路段速度 
    for (start, end), speed in speeds['segment_speeds']['jing_zhong_road']:
        results.append({
            '道路': '经中路', 
            '起点': start,
            '终点': end,
            '路段速度(km/h)': round(speed, 2)
        })

    # 添加平均速度
    results.append({
        '道路': '纬中路平均',
        '起点': '-',
        '终点': '-',
        '路段速度(km/h)': round(speeds['wei_zhong_road_speed'], 2)
    })

    results.append({
        '道路': '经中路平均',
        '起点': '-', 
        '终点': '-',
        '路段速度(km/h)': round(speeds['jing_zhong_road_speed'], 2)
    })

    results.append({
        '道路': '整体平均',
        '起点': '-',
        '终点': '-', 
        '路段速度(km/h)': round(speeds['overall_average_speed'], 2)
    })

    # 转换为DataFrame并保存
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False, encoding='gbk')