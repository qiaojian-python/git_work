// 导包
import Vue from 'vue'
import Vuex from 'vuex'

// 将vuex注入到vue实例中
Vue.use(Vuex)

// 将定义好的vuex导出
export default new Vuex.Store({
    state: {
        count:80,
    },
    mutations: {
        add_count(state){
            state.count++;
        }
    },
    getters: {},
})
