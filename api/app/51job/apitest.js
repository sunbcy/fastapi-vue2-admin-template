xvar = {
  'cfg': {
    '$super': {
      '$super': {
        '$super': {
          '$super': {}
        }
      }
    }
  },
  '_data': {
    'words': [],
    'sigBytes': 0
  },
  '_nDataBytes': 0,
  '_hash': {
    'words': [
      1779033703,
      -1150833019,
      1013904242,
      -1521486534,
      1359893119,
      -1694144372,
      528734635,
      1541459225
    ],
    'sigBytes': 32
  }
}

function generateSign(e) {
  return (0,
  _createHelper)((0,
  _createHelper)(JSON.stringify(e) + nowDate() + 'jmhbz4xv1p8tw9z6umt6cw93bri96iuo').toString()).toString()

  // return (JSON.stringify(e) + nowDate() + 'jmhbz4xv1p8tw9z6umt6cw93bri96iuo').toString().toString()
}

const e = {
  init: function(i) {
    // 初始化逻辑
    console.log('Initializing with:', i)
    return this // 返回当前对象，以便链式调用
  },
  finalize: function(t) {
    // 最终化逻辑
    console.log('Finalizing with:', t)
    return t && _append(t),
    _doFinalize() // 返回一个构造函数或类
  }
}
function _createHelper(t, i) {
  // eslint-disable-next-line new-cap
  return new e.init(i).finalize(t)
}

// u = r.Utf8 = {
//                                 stringify: function(e) {
//                                     try {
//                                         return decodeURIComponent(escape(l.stringify(e)))
//                                     } catch (e) {
//                                         throw new Error("Malformed UTF-8 data")
//                                     }
//                                 },
//                                 parse: function(e) {
//                                     return l.parse(unescape(encodeURIComponent(e)))
//                                 }
//                             }
// function finalize(e) {
//     return e && _append(e),
//     _doFinalize()
// }

function _append(e) {
  typeof e === 'string' && (e = parse(e)),
  this._data.concat(e),
  this._nDataBytes += e.sigBytes
}

function parse(e) {
  return parse11(unescape(encodeURIComponent(e)))
}

function parse11(e) {
  for (var t = e.length, i = [], a = 0; a < t; a++) { i[a >>> 2] |= (255 & e.charCodeAt(a)) << 24 - a % 4 * 8 }
  return new s.init(i, t)
}

function _doFinalize() {
  var e = xvar._data
  var i = e.words
  var a = 8 * xvar._nDataBytes
  var o = 8 * e.sigBytes
  i[o >>> 5] |= 128 << 24 - o % 32
  var n = Math.floor(a / 4294967296)
  var s = a
  i[15 + (o + 64 >>> 9 << 4)] = 16711935 & (n << 8 | n >>> 24) | 4278255360 & (n << 24 | n >>> 8),
  i[14 + (o + 64 >>> 9 << 4)] = 16711935 & (s << 8 | s >>> 24) | 4278255360 & (s << 24 | s >>> 8),
  e.sigBytes = 4 * (i.length + 1),
  xvar._data = {
    'words': [],
    'sigBytes': 0
  }
  for (var r = xvar._hash, c = r.words, l = 0; l < 4; l++) {
    var u = c[l]
    c[l] = 16711935 & (u << 8 | u >>> 24) | 4278255360 & (u << 24 | u >>> 8)
  }
  return r
}

function nowDate() {
  var e = new Date()
  var t = e.getTime()
  var i = 6e4 * e.getTimezoneOffset()
  var a = t + i
  var o = new Date(a + 288e5)
  return o.getFullYear().toString() + (o.getMonth() + 1 < 10 ? '0' + (o.getMonth() + 1) : o.getMonth() + 1).toString() + (o.getDate() < 10 ? '0' + o.getDate() : o.getDate()).toString() + o.getHours().toString()
}

var inputstr = {
  'accountid': '',
  'usertoken': '',
  'client_id': '000011',
  'property': '{"partner":"","webId":2,"fromdomain":"51job_web","frompageUrl":"https://we.51job.com/","pageUrl":"https://we.51job.com/pc/search?jobArea=040000&keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&searchType=2&keywordType=guess_exp_tag6","identityType":"","userType":"","isLogin":"否","accountid":""}',
  'jobArea': '040000',
  'funType': null,
  'keyword': '数据分析'
}

console.log(generateSign(inputstr))
