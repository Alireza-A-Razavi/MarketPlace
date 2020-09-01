import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store=new Vuex.Store({
	state:{
		isSubMenuOpen:false,
		url:null,
		categoriesTop:null,
		isShowFiltering:false,
		isShowUserPanelNavigation:false,
		currentComponentUserPanelNavigation:"profile",
		isShowConsulate:false
	},
	getters:{
		isSubMenu:state=>{
			return state.isSubMenuOpen
		}
	},
	mutations:{
		toggleSubMenu:state=>{
			state.isSubMenuOpen=!state.isSubMenuOpen
		},
		toggleFiltering:state=>{
			state.isShowFiltering=!state.isShowFiltering
		},
		toggleUserPanelNavigation:state=>{
			state.isShowUserPanelNavigation=!state.isShowUserPanelNavigation
		},
		swapUserPanelComponent:(state,payload)=>{
			state.currentComponentUserPanelNavigation=payload
		},
		toggleConsulate:state=>{
			state.isShowConsulate=!state.isShowConsulate
		}
	},
	actions:{
		toggleSubMenu:({commit})=>{
			commit('toggleSubMenu')
		},
		toggleFiltering:({commit})=>{
			commit("toggleFiltering")
		},
		toggleUserPanelNavigation:({commit})=>{
			commit('toggleUserPanelNavigation')
		},
		swapUserPanelComponent:({commit},payload)=>{
			commit('swapUserPanelComponent',payload)
		},
		toggleConsulate:({commit})=>{
			commit("toggleConsulate")
		}

	}
})