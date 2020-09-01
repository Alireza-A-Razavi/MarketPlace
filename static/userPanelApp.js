import vue from 'vue'
import {store} from './userStore.js'
import heading from "./components/user/template/header/header.vue"
import navigation from "./components/user/template/navigation/navigation.vue"
import slicer from './components/user/template/slicer/slicer.vue'
import footer from './components/user/template/footer/footer.vue'
import signup from "./components/user/signup/signup.vue"

const app=new vue({
	el:"#app",
	components:{
		heading,
		navigation,
		slicer,
		foot:footer,
		signup,
		
	},
	store,
	// Router
})