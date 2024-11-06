import service from '@/utils/request'

// 搜索URL
export function sendText(data) {
  return service({
    url: "/qiyewechat/send_text",
    method: 'post',
    data
  })
}