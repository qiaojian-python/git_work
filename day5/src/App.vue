<template>
  <div id="app">

<First></First>
      <hr>
      <Second></Second>
  </div>
</template>

<script>
// 在跟组件将组件导入
import First from './components/First'
import Second from "./components/Second";


export default {
  name: 'App',
  components: {
    First:First,
      Second:Second
  }
}
</script>

<style>

</style>
