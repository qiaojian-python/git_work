<template>
    <div>
        这是Home组件
        <br>
        <input type="text" v-model="msg">
    <button @click="add_note">添加留言</button>
    <ul>
        <li v-for="(u,i) in msg_list" :key="i">
            {{u}}  <span @click="del(i)">删除</span>
        </li>
    </ul>
    <input v-show="count" type="button" value="删除所有" @click="del_all()">
    </div>
</template>

<script>

    export default {
        name: "home",
        data(){
            return{
                msg: '',
                msg_list: localStorage.msgs ? JSON.parse(localStorage.msgs) : [],
                count : '',
            }
        },
        beforeMount(){
            this.s()
        },
        methods: {
            add_note(){
                let msg = this.msg;
                if (msg){
                     this.msg_list.unshift(msg);
                    this.msg = '';
                    localStorage.msgs = JSON.stringify(this.msg_list)
                    this.s()
                }

            },
            // 单个删除
            del(i){
               this.msg_list.splice(i,1)
                localStorage.msgs = JSON.stringify(this.msg_list)
                this.s()
            },
            // 多个删除
            del_all(){
                this.msg_list = []
                localStorage.removeItem('msgs')
                this.s()
            },
            // 按钮更新以及 持久化存储删除
            s(){
                if (this.msg_list.length == 0){
                    this.count = false
                } else {
                    this.count = true
                }

            }
        },
    }
</script>

<style scoped>

</style>
