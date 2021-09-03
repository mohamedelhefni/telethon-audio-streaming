import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import store from './store'
import "./index.css";

createApp(App).use(store).mount('#app')
