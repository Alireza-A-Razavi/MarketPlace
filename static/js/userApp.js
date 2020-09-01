import vue from 'vue'
import vueRouter from 'vue-router'
import {store} from './userStore.js'
import heading from "./components/user/template/header/header.vue"
import index from "./components/user/index/index.vue"
import navigation from "./components/user/template/navigation/navigation.vue"
import slicer from './components/user/template/slicer/slicer.vue'
import footer from './components/user/template/footer/footer.vue'
import product from "./components/user/product/product.vue"
import productZoom from './components/user/product/productZoom.vue'
import signup from "./components/user/signup/signup.vue"
import products from "./components/user/prodcuts/products.vue"
import filtering from "./components/user/prodcuts/filtering.vue"
import userPanel from "./components/user/userPanel/userPanel.vue"
import category from "./components/user/category/category.vue"
import doneMessage from './components/user/template/doneMessage/doneMessage.vue'
import {routes} from "./routes.js"
vue.use(vueRouter)

const router=new vueRouter({
	routes,
	mode:"history"
})
const app=new vue({
	el:"#app",
	components:{
		heading,
		index,
		navigation,
		slicer,
		foot:footer,
		product,
		productZoom,
		signup,
		products,
		filtering,
		userPanel,
		category,
		doneMessage
	},
	store,
	router,
	// Router
})