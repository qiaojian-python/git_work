<template>
<div>
    这是User组件
    <br>
    <h3>用户列表页</h3>
    <table border="2">
        <tr>
            <td>ID</td>
            <td>姓名</td>
            <td>生日</td>
            <td>个人信息</td>
            <td>操作</td>
        </tr>
        <tr v-for="(user,i) in users" :key="user.id">
            <td>{{user.id}}</td>
            <td>{{user.username}}</td>
            <td>{{user.bir}}</td>
            <td>{{user.content}}</td>
            <td><span @click="del(i)">删除</span> |
                <router-link :to="`/detail/${user.id}/${user.username}/${user.bir}/${user.content}/`">
                    查看用户详情</router-link></td>
        </tr>

    </table>
    <hr>
        用户名: <input type="text" v-model="username"> <br>
        生日: <input type="text" v-model="bir"> <br>
        个人信息: <input type="text" v-model="content"> <br>
        <button @click="addUser">添加用户</button>

</div>
</template>

<script>
    export default {
        name: "User",
        data(){
            return {
                // users: [
                //     {'id':1,username:"小黑",bir:"2020-1-1",content:"我是小黑"},
                //     {'id':2,username:"小白",bir:"2020-2-2",content:"我是小白"},
                //     {'id':3,username:"小天",bir:"2020-3-3",content:"我是小天"},
                // ],
                users: localStorage.userlist ? JSON.parse(localStorage.userlist) : [],
                username: '',
                bir: '',
                content: '',

            }
        },
        methods :{
            addUser(){
                if (this.username && this.content && this.bir) {
                    let user = {'id':this.users.length + 1, username:this.username,bir:this.bir,content:this.content}
                    this.users.push(user)
                    localStorage.userlist = JSON.stringify(this.users)
                    this.username = ''
                    this.bir = ''
                    this.content = ''
                }

            },
            del(i){
                this.users.splice(i,1)
                localStorage.userlist = JSON.stringify(this.users)
            }
        }
    }
</script>

<style scoped>

</style>
