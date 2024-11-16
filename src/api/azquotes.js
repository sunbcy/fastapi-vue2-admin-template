import service from '@/utils/request'

// 搜索URL
export async function getTodayQuote() {
  try {
    return await service({
      url: '/azquotes',
      method: 'get'
    }) // 假设 response.data 是你期望的返回数据
  } catch (error) {
    console.error('获取今日格言失败:', error)
    throw error // 重新抛出错误以便上层处理
  }
}
