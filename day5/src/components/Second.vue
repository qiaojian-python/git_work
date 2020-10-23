<template>
    <div>
        <p>这是我的第二个组件</p>

        <h3>{{username}}</h3>
        <span @click="clickme">{{number}}</span>

    </div>
</template>

<script>
    export default {
        name: "Second",
        data: function () {
            return {
                username: '小黑',
                number: 30,
            }
        },
        methods:{
            clickme(){
                this.number --;
            }
        }
    }
</script>

<style scoped>

</style>
