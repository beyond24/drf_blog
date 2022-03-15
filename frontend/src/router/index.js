import {createWebHistory, createRouter} from "vue-router";
import HomePage from "@/views/HomePage";
import ArticleDetail from "@/views/ArticleDetail";
import LoginPage from "@/views/LoginPage";
import UserCenter from "@/views/UserCenter.vue";


const routes = [
    {
        path:"/",
        name:"HomePage",
        component:HomePage,
    },
    {
        path:"/article/:id",
        name:"ArticleDetail",
        component:ArticleDetail,
    },
    {
        path:"/login",
        name:"LoginPage",
        component:LoginPage,
    },
     {
        path: "/user/:username",
        name: "UserCenter",
        component: UserCenter
    },
];

const router = createRouter({
    history:createWebHistory(),
    routes,
});

export default router;