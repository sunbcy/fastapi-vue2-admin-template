import service from '@/utils/request'

// 搜索URL
export function search_jobs(data) {
  return service({
    url: "/liepin/get_jobs",
    method: 'post',
    data
  })
}

export function getJobDetails(data) {
  return service({
    url: "/liepin/getJobDetails",
    method: 'post',
    data
  })
}

export function get_job_num() {
  return service({
    url: "/liepin/get_job_num",
    method: 'get'
  })
}

export function get_comp_num() {
  return service({
    url: "/liepin/get_comp_num",
    method: 'get'
  })
}

export function get_top_ten_industries() {
  return service({
    url: "/liepin/get_top_ten_industries",
    method: 'get'
  })
}