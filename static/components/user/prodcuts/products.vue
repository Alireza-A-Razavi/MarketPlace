<template>
    <div id="products">
        <div class="filterText">
           <button class='submit' @click='toggleFiltering()'>فیلتر محصولات</button>
        </div>
        <div @click='toggleConsulate(),adjustConsulateTop()' class="speek">
            <p>مشاوره رایگان</p>
        </div>
        <div id="productsWrapper">
            <div class="product">
                <div class="productImg">
                    <img src="/images/ampl.jpg" alt="">
                </div>
                <div class="descs">
                    <div class="productTitle">
                        <p><a href="#">امپلی فایر مدل PA system S30-/60M</a></p>
                    </div>
                    <div class="productDescs">
                        <p>{{getDescs(descs)}}</p>
                    </div>
                </div>
                <div class="productRegion">
                    <div class="compony">
                        <p>ساخت گلد ایران ایران ایران ایرن</p>
                    </div>
                    <div class="region">
                        <p>چین</p>
                        <img src="/images/china.png" alt="china"> 
                        
                    </div>
                    <div class="seeProduct">
                        <a class='submit' href="#">مشاهده محصول</a>
                    </div>
                </div>
            </div>


            <hr>


            <div class="product">
                <div class="productImg">
                    <img src="/images/ampl.jpg" alt="">
                </div>
                <div class="descs">
                    <div class="productTitle">
                        <p><a href="#">امپلی فایر مدل PA system S30-/60M</a></p>
                    </div>
                    <div class="productDescs">
                        <p>{{getDescs(descs)}}</p>
                    </div>
                </div>
                <div class="productRegion">
                    <div class="compony">
                        <p>ساخت گلد ایران ایران ایران ایرن</p>
                    </div>
                    <div class="region">
                        <p>چین</p>
                        <img src="/images/china.png" alt="china">
                        
                    </div>
                    <div class="seeProduct">
                        <a class='submit' href="#">مشاهده محصول</a>
                    </div>
                </div>
            </div>





        </div>
        <transition name="fade" mode='out-in'>
            <consulate :key='hello'></consulate>
        </transition>
    </div>
</template>

<style scoped>
    .speek{
        background: rgb(229,46,113);
        position:fixed;
        right:0;
        top:200px;
        z-index:665;
        cursor:pointer
    }
    .speek p{
        padding:10px;
        color:white;
        font-size:10pt;
        
    }
    .filterText{
        width:100%;
        display:flex;
        justify-content: center;
        margin-top:10px
    }
    #products{
        display:flex;
        flex-direction: column;
        align-items: flex-end;
        background: white;
        margin-top:20px
    }
    #productsWrapper{
        padding:10px;
    }
    .product{
        display:flex;
        justify-content: space-between;
    }
    .product:not(:first-child)
    {
        margin-top:20px
    }
    .descs{
        display:flex;
        flex-direction:column;
        align-items: flex-end;
        width:60%;
    }
    .productTitle a{
        color:rgb(74, 96, 192)
    }

    .region img{
        width:40px;
        height: 30px;
    }
    .productImg{
        order:3;
        display:flex;
        justify-content: center;
        align-items: center;
    }
    .productDescs p{
        font-size:14pt
    }
    .compony p{
        font-size:12pt
    }
    .productImg img{
        width:200px;
        height:200px
    }
    .seeProduct{
        margin-top:20px
    }
    .productRegion{
        display:flex;
        flex-direction:column;
        justify-content:flex-start;
        align-items: center;
        border:5px solid rgb(211, 219, 221)
    }
    .productRegion div{
        padding:5px
    }
    .descs{
        order:2
    }
    .productRegion{
        order:1
    }
    .region{
        display:flex
    }
    .productImg img:hover{
        transform: scale(1.4);
    }
    @media (max-width:815px)
    {
        .product{
            flex-direction: column;
        }
        .descs
        {
            width:100%
        }
        .productRegion{
            order:3
        }
        .productImg{
            order:1
        }
        .productRegion{
            height: 150px;
            max-width: max-content;
            margin:auto
        }
        .productTitle p{
            font-size: 15pt;
            line-height: 120%;
        }
        .productDescs p{
            line-height: 120%;
        }
        .productRegion{
            margin-top:20px
        }
    }
    .fade-enter-active{
        animation: fadeIn 0.3s linear;
    }
    .fade-leave-active{
        animation: fadeOut 0.3s linear;
    }
    @keyframes fadeIn {
        from{
            opacity: 0;
        }
        to{
            opacity: 1;
        }
    }
    @keyframes fadeOut {
        from{
            opacity: 1;
        }
        to{
            opacity: 0;
        }
    }

</style>

<script>
    import {mapActions} from 'vuex'
    import consulate from "./consulate.vue"
    export default{
        components:{
            consulate
        },
        data(){
            return{
                descs:'محصول ساخت چین قدرت تولید صدا تا 1200 دسیبل دارای باتری 36 ولت فلان لان فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان لان فلان فلان الن'
            }
        },
        methods:{
            ...mapActions([
               'toggleFiltering',
               'toggleConsulate'
            ]),
            getDescs(){
                return this.descs.length>100 ? this.descs.substring(0,200)+'...' : this.descs
            },
            adjustConsulateTop(){
                const consulate=document.querySelector("#consulateWrapper")
                consulate.style.top=window.scrollY+100+"px"
                document.body.style.overflow='hidden'
                const done=document.querySelector("#doneMessage")
                done.style.display='none'
            }
        },
        props:["products"],
        created(){
            console.log(products)
        }
    }
</script>