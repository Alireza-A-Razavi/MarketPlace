<template>
    <div id="userPanel" class='mainItemForUserPanel'>
        <div id="userPanelWrapper">
            <div id="userPanelNavigationWrapper">
                <button class='submit' @click='toggleUserPanelNavigation'>منوی کاربری</button>
            </div>
            
            <user-panel-navigation></user-panel-navigation>

                <transition name="router" mode="out-in">
                    <router-view/>
                
                </transition>
            
        </div>
        
    </div>    
</template>

<script>
    import {mapActions} from 'vuex'
    import userPanelNavigation from "./userPanelNavigation.vue"
    // import createProduct from "./createPRoduct/createProduct.vue"
    // import profile from "./profile/profile.vue"
    export default{
        name:"userPanel",
        components:{
            userPanelNavigation,
            // createProduct,
            // profile
        },
        methods:{
            ...mapActions([
                'toggleUserPanelNavigation'
            ]),
            // getcCrrenComponent(){
            //     return this.$store.state.currentComponentUserPanelNavigation
            // }
        }
    }
</script>


<style scoped>
    #userPanel{
        margin-top:20px;

    }
    #userPanelWrapper{
        display:flex;
        width:100%;
        align-content: center;
        flex-direction:column;
    }
    #userPanelNavigationWrapper{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .submit{
        max-width:max-content
    }
    .userPanelComp{
        background: white;
    }
    .router-enter-active{
        opacity:0;
        animation:expnad 0.5s linear forwards;
    }
    .router-leave-active{
        opacity:1;
        animation:expnadOff 0.5s linear forwards;
    }
    @keyframes expnad {
        from{
            opacity: 0
        }
        to{
            opacity: 1
        }
    }
    @keyframes expnadOff {
        from{
            opacity: 1
        }
        to{
            opacity: 0
        }
    }


</style>