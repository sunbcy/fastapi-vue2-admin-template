import service from '@/utils/request'

// 搜索URL
export async function search_jobs(data) {
  return await service({
    url: '/liepin/get_jobs',
    method: 'post',
    data
  })
}

export async function getJobDetails(data) {
  return await service({
    url: '/liepin/getJobDetails',
    method: 'post',
    data
  })
}

export async function get_job_num() {
  return await service({
    url: '/liepin/get_job_num',
    method: 'get'
  })
}

export async function get_comp_num() {
  return await service({
    url: '/liepin/get_comp_num',
    method: 'get'
  })
}

export async function get_top_ten_industries() {
  return await service({
    url: '/liepin/get_top_ten_industries',
    method: 'get'
  })
}
