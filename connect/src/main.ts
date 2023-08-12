import './assets/main.css'

import { createApp } from 'vue'
import './assets/main.css'
import axios from 'axios'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
app.config.globalProperties.$http = axios

app.use(createPinia())

app.mount('#app')
