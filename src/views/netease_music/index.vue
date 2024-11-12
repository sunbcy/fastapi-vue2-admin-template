<template>
  <div class="full-height-container">
    <!-- 搜索栏和搜索按钮 -->
    <el-row :gutter="20" style="margin-left: 10px; height: 100%">
      <el-col :span="16" class="grid-content; height: 100%;">
        <!-- 搜索输入框 -->
        <el-col :span="24" class="grid-content; height: 100%;">
          <h4 class="text-gray-700 text-lg mb-4">用户id->歌单id列表</h4>
          <el-col :span="14" class="grid-content; height: 100%;">
            <el-input
              v-model="searchText"
              placeholder="请输入你的用户id"
              @keyup.enter="onSearch"
            />
          </el-col>
          <el-col :span="2" class="grid-content; height: 100%;">
            <el-button
              type="primary"
              icon="el-icon-search"
              @click="onSearch"
            >搜索
            </el-button>
          </el-col>
        </el-col>

        <el-col :span="24" class="grid-content; height: 100%;">
          <h4 class="text-gray-700 text-lg mb-4">歌单id->歌曲id列表</h4>
          <el-col :span="14" class="grid-content; height: 100%;">
            <el-input
              v-model="playlistid_searchSongs"
              placeholder="请输入你的歌单id"
              @keyup.enter="onSearchSongs"
            />
          </el-col>
          <el-col :span="2" class="grid-content; height: 100%;">
            <el-button
              type="primary"
              icon="el-icon-search"
              @click="onSearchSongs"
            >搜索
            </el-button>
          </el-col>
        </el-col>

        <el-col :span="24" class="grid-content; height: 100%;">
          <h4 class="text-gray-700 text-lg mb-4">歌曲id->歌曲详情</h4>
          <el-col :span="14" class="grid-content; height: 100%;">
            <el-input
              v-model="song_searchDetail"
              placeholder="请输入你的歌曲id"
              @keyup.enter="onSearchSong"
            />
          </el-col>
          <!-- 搜索按钮 -->
          <el-col :span="2" class="grid-content; height: 100%;">
            <el-button
              type="primary"
              icon="el-icon-search"
              @click="onSearchSong"
            >搜索
            </el-button>
          </el-col>
        </el-col>

        <el-col :span="24" class="grid-content; height: 100%;">
          <h4 class="text-gray-700 text-lg mb-4">歌曲id->歌曲url</h4>
          <el-col :span="14" class="grid-content; height: 100%;">
            <el-input
              v-model="songid_searchSongUrl"
              placeholder="请输入你的歌曲id"
              @keyup.enter="onSearchSongUrl"
            />
          </el-col>
          <!-- 搜索按钮 -->
          <el-col :span="2" class="grid-content; height: 100%;">
            <el-button
              type="primary"
              icon="el-icon-search"
              @click="onSearchSongUrl"
            >搜索
            </el-button>
          </el-col>
        </el-col>

        <el-col :span="24" class="grid-content; height: 100%;">
          <h4 class="text-gray-700 text-lg mb-4">歌曲id->歌曲lyric</h4>
          <el-col :span="14" class="grid-content; height: 100%;">
            <el-input
              v-model="songid_searchSongLyric"
              placeholder="请输入你的歌曲id"
              @keyup.enter="onSearchSongLyric"
            />
          </el-col>
          <!-- 搜索按钮 -->
          <el-col :span="2" class="grid-content; height: 100%;">
            <el-button
              type="primary"
              icon="el-icon-search"
              @click="onSearchSongLyric"
            >搜索
            </el-button>
          </el-col>
        </el-col>

        <el-col :span="24" class="grid-content; height: 100%;">
          <h4 class="text-gray-700 text-lg mb-4">歌曲id->歌曲comments</h4>
          <el-col :span="14" class="grid-content; height: 100%;">
            <el-input
              v-model="songid_searchSongComments"
              placeholder="请输入你的歌曲id"
              @keyup.enter="onSearchSongComments"
            />
          </el-col>
          <!-- 搜索按钮 -->
          <el-col :span="2" class="grid-content; height: 100%;">
            <el-button
              type="primary"
              icon="el-icon-search"
              @click="onSearchSongComments"
            >搜索
            </el-button>
          </el-col>
        </el-col>
      </el-col>

      <el-col :span="8" class="grid-content; height: 100%; ">
        <div class="scrollable-content">
          <div v-if="currentView === 'search_songlist_id'">
            <!-- 这里放置你的组件或内容 -->
            <!-- 搜索结果显示 -->
            <h4 class="text-gray-700 text-lg mb-4">
              搜索结果
            </h4>
            <!-- 这里假设你的搜索结果是一个表格 -->
            <el-table
              :data="tableData"
              stripe
              style="padding: 2px; overflow-y: auto;"
            >
              <el-table-column prop="id" label="歌单id" width="150" />
              <el-table-column prop="name" label="歌单名" width="150" />
              <!-- 在这里添加你的表格列 -->
            </el-table>
          </div>

          <div v-if="currentView === 'search_song_id'">
            <h4 class="text-gray-700 text-lg mb-4">
              搜索结果
            </h4>
            <div v-if="song_detailResult">
              <div v-if="song_detailResult.al && song_detailResult.al.picUrl" class="avatar-container">
                <img :src="song_detailResult.al.picUrl" alt="专辑封面" class="album-cover">
              </div>
              <br>
              <div v-if="songid_searchSongUrlResult">
                <a :href="songid_searchSongUrlResult" target="_blank" rel="noopener noreferrer" class="song-link">
                  {{ song_detailResult.name }}
                </a>
              </div>
              <br>
              <!--              <span> {{ songid_searchSongUrlResult }}</span>-->
              <!--              <br>-->
              <span> {{ song_detailResult.id }}</span>
              <br>
              <span> {{ song_detailResult.ar[0].name }}</span>
              <br>
              <span> {{ song_detailResult.al.name }}</span>
              <br>
              <div v-if="songid_searchSongLyricResult">
                <div v-html="formattedLyric" />
              </div>
            </div>
          </div>

          <div v-if="currentView === 'search_songs_playlistid'">
            <h4 class="text-gray-700 text-lg mb-4">
              搜索结果
            </h4>
            <el-table
              :data="songs_tableData"
              stripe
              style="padding: 2px; overflow-y: auto;"
            >
              <el-table-column prop="id" label="歌曲id" width="150" />
              <el-table-column prop="uid" label="用户id" width="150" />
              <!-- 在这里添加你的表格列 -->
            </el-table>
          </div>

          <div v-if="currentView === 'search_songs_musicurl'">
            <h4 class="text-gray-700 text-lg mb-4">
              搜索结果
            </h4>
            <div v-if="songid_searchSongUrlResult">
              <br>
              <div v-if="songid_searchSongUrlResult">
                <a :href="songid_searchSongUrlResult" target="_blank" rel="noopener noreferrer" class="song-link">
                  点击这里听歌
                </a>
              </div>
              <span> {{ songid_searchSongUrlResult }}</span>
              <br>
            </div>
          </div>

          <div v-if="currentView === 'search_songs_musiclyric'">
            <h4 class="text-gray-700 text-lg mb-4">
              搜索结果
            </h4>
            <div v-if="songid_searchSongLyricResult">
              <div v-html="formattedLyric" />
            </div>
          </div>

          <div v-if="currentView === 'search_songs_musiccomments'">
            <h4 class="text-gray-700 text-lg mb-4">
              搜索结果
            </h4>
            <div class="search-results">
              <div v-if="songid_searchSongCommentsResult">
                <!--              <span> {{ songid_searchSongCommentsResult }}</span>-->
                <div v-for="result in songid_searchSongCommentsResult" :key="result.commentId" class="card">
                  <div v-if="result.user_avatarUrl" class="avatar-container-1">
                    <img :src="result.user_avatarUrl" alt="头像" class="album-cover-1">
                    <h4><span class="stock-num">{{ result.nickname }} {{ result.vipType }}</span></h4>
                  </div>
                  <h4>{{ result.content }}</h4>
                  <h4><span class="stock-num">{{ result.extInfo_endpoint.CLIENT_VERSION_STR }}</span>
                    {{ result.extInfo_endpoint.CLIENT_SIGN }} {{ result.extInfo_endpoint.CHANNEL }}
                    {{ result.extInfo_endpoint.CLIENT_TYPE }} {{ result.extInfo_endpoint.OS_TYPE }}
                    {{ result.extInfo_endpoint.OSVER }}</h4>
                  <!--                  <p>USER_AGENT： {{ result.extInfo_endpoint.USER_AGENT }}</p>-->
                  <!--                  <p>X_REMOTE_PORT：{{ result.extInfo_endpoint.X_REMOTE_PORT }}</p>-->
                  <p>ipLocation：{{ result.extInfo_endpoint.IP }}-{{ result.ipLocation.location }}</p>
                  <p>liked：{{ result.liked }}</p>
                  <p>likedCount：{{ result.likedCount }}</p>
                  <p>time：{{ result.time }}</p>
                  <p>timeStr：{{ result.timeStr }}</p>
                  <p>userId：{{ result.userId }}</p>
                  <p>userType：{{ result.userType }}</p>
                  <p>user_followed：{{ result.user_followed }}</p>
                  <p>user_isHug：{{ result.user_isHug }}</p>
                  <p>vipRights：{{ result.vipRights }}</p>
                  <div v-if="result.beReplied">
                    <div v-for="sub_result in result.beReplied" :key="sub_result.beRepliedCommentId" class="card">
                      <div v-if="sub_result.user.avatarUrl" class="avatar-container-1">
                        <img :src="sub_result.user.avatarUrl" alt="头像" class="album-cover-1">
                        <h4><span class="stock-num">{{ sub_result.user.nickname }} {{ sub_result.user.vipType }}</span></h4>
                      </div>
                      <h4> {{ sub_result.content }} </h4>
                      <p>ipLocation：{{ getIP() }}-{{ sub_result.ipLocation.location }}</p>
                      <!--                      <p>涨跌幅：<span style="color: red;">{{ sub_result.article.action_info.shares_range / 100 }} %</span></p>-->
                      <!--                      <p>涨停时间：{{ sub_result.article.action_info.time }}</p>-->
                      <!--                      <p>解析：{{ sub_result.article.action_info.expound }}</p>-->
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </el-col>
    </el-row>
  </div>

</template>

<script>
import { sid_searchComments, sid_searchLyric, sid_searchUrl, pid_searchKeyword, searchKeywords, songsearchKeywords } from '@/api/163_music'

export default {
  data() {
    return {
      currentView: 'search_songlist_id', // 默认显示搜索结果
      // searchText: '周杰伦', // 绑定在搜索框上的模型
      searchText: '252904283', // 默认歌单id
      song_searchDetail: '1869285', // 默认歌曲id
      playlistid_searchSongs: '9394881313',
      tableData: [], // 用于存放搜索结果的数据
      song_detailResult: null,
      // songs_searchPlaylistid: null,
      songs_tableData: [],
      songid_searchSongUrl: '191060', // 默认歌曲id
      songid_searchSongUrlResult: null,
      songid_searchSongLyric: '191060', // 默认歌曲id
      songid_searchSongLyricResult: null,
      songid_searchSongComments: '1913206466', // 默认歌曲id
      songid_searchSongCommentsResult: []
    }
  },
  computed: {
    formattedLyric() {
      return this.songid_searchSongLyricResult.replace(/\n/g, '<br>')
    }
  },
  mounted() {
    setTimeout(this.onSearchSong(), 500)
  },
  methods: {
    async onSearch() {
      // 触发搜索逻辑
      const s_data = {
        'searchText': this.searchText
      }
      try {
        const res = await searchKeywords(s_data)
        this.tableData = res.searchResults // -->
        console.log(this.tableData)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }
      this.currentView = 'search_songlist_id'
    },
    async onSearchSong() {
      // 触发搜索逻辑
      const ss_data = {
        'song_searchDetail': this.song_searchDetail,
        'songid_searchSongUrl': this.song_searchDetail,
        'songid_searchSongLyric': this.song_searchDetail
      }
      try {
        const res = await sid_searchUrl(ss_data)
        this.songid_searchSongUrlResult = res.searchResults // -->
        console.log(this.songid_searchSongUrlResult)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }

      try {
        const res = await songsearchKeywords(ss_data)
        this.song_detailResult = res.searchResults
        console.log(this.song_detailResult.name)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }

      try {
        const res = await sid_searchLyric(ss_data)
        this.songid_searchSongLyricResult = res.searchResults // -->
        console.log(this.songid_searchSongLyricResult)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }
      this.currentView = 'search_song_id'
    },
    async onSearchSongs() {
      // 触发搜索逻辑
      const sss_data = {
        'playlistid_searchSongs': this.playlistid_searchSongs
      }
      try {
        const res = await pid_searchKeyword(sss_data)
        this.songs_tableData = res.searchResults // -->
        console.log(this.songs_tableData)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }
      this.currentView = 'search_songs_playlistid'
    },
    async onSearchSongUrl() {
      // 触发搜索逻辑
      const ssss_data = {
        'songid_searchSongUrl': this.songid_searchSongUrl
      }
      try {
        const res = await sid_searchUrl(ssss_data)
        this.songid_searchSongUrlResult = res.searchResults // -->
        console.log(this.songid_searchSongUrlResult)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }
      this.currentView = 'search_songs_musicurl'
    },
    async onSearchSongLyric() {
      // 触发搜索逻辑
      const sssss_data = {
        'songid_searchSongLyric': this.songid_searchSongLyric
      }
      try {
        const res = await sid_searchLyric(sssss_data)
        this.songid_searchSongLyricResult = res.searchResults // -->
        console.log(this.songid_searchSongLyricResult)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }
      this.currentView = 'search_songs_musiclyric'
    },
    async onSearchSongComments() {
      // 触发搜索逻辑
      const ssssss_data = {
        'songid_searchSongComments': this.songid_searchSongComments
      }
      try {
        const res = await sid_searchComments(ssssss_data)
        this.songid_searchSongCommentsResult = res.searchResults // -->
        console.log(this.songid_searchSongCommentsResult)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 发送失败.')
      }
      this.currentView = 'search_songs_musiccomments'
    },
    getIP() {
      // 使用三元运算符来选择 IP 地址
      return this.sub_result?.extInfo_endpoint?.IP || this.sub_result?.ipLocation?.ip
    }
  }
}
</script>

<style scoped>
/* 确保从 html 到 body 都是 100% 高度 */
.full-height-container {
  height: 100%;
  margin: 0;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.mb-4, .my-4 {
  margin-bottom: 1.5rem !important;
}

.scrollable-content {
  //height: 100%;
  height: 90vh;  /* 设置容器高度为视口高度 */
  overflow-y: auto; /* 使内容可滚动 */
  padding: 10px; /* 可选：内边距 */
}

.avatar-container {
  display: flex;
  justify-content: left;  /* 水平居中 */
  align-items: center;      /* 垂直居中 */
  margin-top: 20px;         /* 可选：添加一些顶部间距 */
}

.album-cover {
  width: 100px;  /* 你可以根据需要调整宽度 */
  height: auto;  /* 保持图片的宽高比 */
  border-radius: 90%;  /* 使图片呈现圆形 */
  object-fit: cover;  /* 保持图片的比例并裁剪以适应容器 */
  margin-top: 10px;  /* 可选：添加一些顶部间距 */
}

.avatar-container-1 {
  display: flex;
  justify-content: left;  /* 水平居中 */
  align-items: center;      /* 垂直居中 */
  margin-top: 0;         /* 可选：添加一些顶部间距 */
}

.album-cover-1 {
  width: 30px;  /* 你可以根据需要调整宽度 */
  height: auto;  /* 保持图片的宽高比 */
  border-radius: 90%;  /* 使图片呈现圆形 */
  object-fit: cover;  /* 保持图片的比例并裁剪以适应容器 */
  margin-top: 0;  /* 可选：添加一些顶部间距 */
}

.song-link {
  display: inline-block;
  margin-top: 10px;
  color: #007bff;  /* 链接颜色 */
  text-decoration: none;  /* 去掉下划线 */
  font-weight: bold;  /* 加粗字体 */
}

.song-link:hover {
  text-decoration: underline;  /* 鼠标悬停时显示下划线 */
}

  .stock-num {
    font-weight: bold;
    font-size: 12px;
    color: #888;
  }

  .search-results {
    display: flex;
    flex-direction: column; /*卡片竖向排列 */
  }

  .card {
    width: 98%;
    padding: 2px;
    margin: 1px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow:0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
  }

  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  h3 {
    margin: 0 0 2px;
  }

  .card h4 {
    margin: 0 0 2px;
  }

  p {
    margin: 0;
  }
</style>
