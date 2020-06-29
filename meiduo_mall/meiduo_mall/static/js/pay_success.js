var vm = new Vue({
    el: '#app',
	// 修改Vue变量的读取语法，避免和django模板语法冲突
    delimiters: ['[[', ']]'],
    data: {
        username: ''
    },
    mounted(){
        this.username=getCookie('username');
    },
    methods: {
    }
});
