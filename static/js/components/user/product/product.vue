<template>
    <div id="product" class='mainItemPerPage'>
        <div id="productWrapper">
            <prudctDetail></prudctDetail>
            <hr>
            <div class="chooseSection">
                <div class="section">
                    <p @click='currentComponent="commentSection"'>نظرات کاربران</p>
                </div>
                <div class="section">
                    <p @click='currentComponent="componyDetali"'>مشخصات شرکت</p>
                </div>
                <div class="section">
                    <p @click='currentComponent="productDescs"'>توضیحات محصول</p>
                </div>
            </div>
            <hr>
            <transition name="swapComp" mode="out-in">
                <component :is="currentComponent"></component>

            </transition>
        </div>


    </div>


</template>

<script>
    import prudctDetail from "./productDetaile.vue"
    import commentSection from './commentSection.vue'
    import productDescs from './productDescs.vue'
    import componyDetali from "./componyDetail.vue"
    export default{
        data(){
            return{
                currentComponent:'commentSection'
            }
        },
        name:"product",
        components:{
            prudctDetail,
            commentSection,
            productDescs,
            componyDetali
        }

    }
</script>




<style>
    #product{
        background:white
    }
    
    #productDetail{
        grid-area:productDetail
    }
    #productComments{
        grid-area:productComments
    }
    #productWrapper{
        display:flex;
        flex-direction:column
    }
    .chooseSection{
        display:flex;
        justify-content: center;
        border-bottom:1px solid rgb(209, 196, 196)
    }
    .section{
        border:1px solid rgb(209, 196, 196);
        margin:5px;
        cursor:pointer
    }
    .chooseSection p{
        padding:10px;
        color:rgb(105, 98, 209)
    }
    @media (max-width:509px)
    {
        .chooseSection{
            flex-direction:column;
            align-items: center;
        }
        .section{
            width:200px;
            display:flex;
            justify-content: center;
        }
        .section p{
            max-width:max-content
        }
    }
    .swapComp-enter-active{
        animation:comeIn 0.25s linear
    }
    .swapComp-leave-active{
        animation:comeOut 0.25s linear
    }
    @keyframes comeIn {
        from{
            opacity:0
        }
        to{
            opacity: 1;
        }
    }

    @keyframes comeOut {
        from{
            opacity:1
        }
        to{
            opacity: 0;
        }
    }

</style>