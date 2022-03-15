import { createApp } from 'vue'
import App from './App.vue'

// createApp(App).mount('#app')

import router from './router'
// 因为 main.js 在 Vue 初始化时必然会执行，URLSearchParams 对象就有了这个 appendIfExists()
URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};

createApp(App).use(router).mount('#app');