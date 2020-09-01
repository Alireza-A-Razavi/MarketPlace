<template >
        <div id="productDetail">
            
            <div class="productDetailWrapper">
                <div class="prodcuctName">
                    <p>بیل مکانیکی</p>
                </div>
                <div class="productDetails">
                    <div class="productDetailsWrap">
                        <div class="productImgAndOther">
                            <div class="productImg">
                                <img class='photo' src="/images/b.jpg" alt="">
                                <!-- <div class="productImage"></div> -->
                                <div @click='zoomIn()'><img class='zoomSign' src="/images/mag.png" alt=""><p>بزرگنمایی</p></div>
                                <div class='numbers'><p>مانده:<span>ناموجود</span></p></div>
                            </div>
                        </div>
                        <div class="productSingleDetailWrapper">
                            <div class="justReadableDetailWrapper">
                                <div class="price singleDetail">
                                    <div class='order1'><p>قیمت:</p></div>
                                    <div class='order2'><p>100 تومن</p></div>
                                </div>
                                <div class="price singleDetail">
                                    <div class='order1'><p>ساخت:</p></div>
                                    <div class='order2'><p>ایران</p></div>
                                </div>

                                <div class="price singleDetail">
                                    <div class='order1'><p>رنگ:</p></div>
                                    <div class='order2'><p>سفید , سیاه , خاکستری</p></div>
                                </div>
                                <div class="price singleDetail">
                                    <div class='order1'><p>جنس:</p></div>
                                    <div class='order2'><p>فولاد</p></div>
                                </div>
                                <div class="price singleDetail">
                                    <div class='order1'><p>وزن:</p></div>
                                    <div class='order2'><p>150 کیلو</p></div>
                                </div>
                                <div class="price singleDetail">
                                    <div class='order1'><p>حداقل تعداد قابل خرید:</p></div>
                                    <div class='order2'><p>5</p></div>
                                </div>
                                <div class="price singleDetail">
                                    <div class='order1'><p>حذاکثر تعداد قابل خرید:</p></div>
                                    <div class='order2'><p>100</p></div>
                                </div>
                                <div class="price singleDetail">
                                    <div class='order1'><p>ارائه نمونه:</p></div>
                                    <div class='order2'><p>بله</p></div>
                                </div>
                                <div class="price singleDetail">
                                    <div class='order1'><p>امتیاز:</p></div>
                                    <div class='order2'><p>4.5</p></div>
                                </div>
                                <div class="rating">
                                    <div class="star">
                                        <star-rating :fixed-points="2" :increment="0.01"></star-rating>
                                    </div>
                                </div>
                                <input type="hidden" :value="payWay">
                                <input type="hidden" :value="packetType">
                                <input type="hidden" :value="sendWay">
                            </div>
                            <div class="writeAbleDetaile">
                                <div class="writeAbleDetaileWrapper">
                                    <div class="payWayWrapper writeAbleSignleItem">
                                        
                                        <div class="sendWayBtns writeAbleSignleItemBtns">
                                            <button @click='chageneSendWay($event),changeButtonColor($event)' class='selectAbleBtns'>زمینی</button>
                                            <button @click='chageneSendWay($event),changeButtonColor($event)' class='selectAbleBtns'>هوایی</button>
                                        </div>
                                        <div class="writeAbleSignleItemTitle">
                                            <p>روش ارسال را انتخاب کنید</p>
                                        </div>
                                    </div>
                                    <div class="packTypeWrapper writeAbleSignleItem">
                                        
                                        <div class="packTypeBtns writeAbleSignleItemBtns">
                                            <button @click='changePacketType($event),changeButtonColor($event)' class='selectAbleBtns'>کاغذی</button>
                                            <button @click='changePacketType($event),changeButtonColor($event)' class='selectAbleBtns'>فلزی</button>
                                        </div>
                                        <div class="writeAbleSignleItemTitle">
                                            <p>بسته بندی</p>
                                        </div>
                                    </div>

                                    <div class="payWay writeAbleSignleItem">
                                        <div class="writeAbleSignleItemBtns">
                                            <button @click='changePayWay($event),changeButtonColor($event)' class='selectAbleBtns'>حضوری</button>
                                            <button @click='changePayWay($event),changeButtonColor($event)' class='selectAbleBtns'>انلاین</button>
                                        </div>
                                        <div class="writeAbleSignleItemTitle">
                                            <p>روش پرداخت:</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
import ImageZoom from 'js-image-zoom'
import starRating from 'vue-star-rating'
    export default {
        components:{
            starRating
        },
        data(){
            return{
                payWay:null,
                packetType:null,
                sendWay:null
            }
        },
        methods:{
            zoomIn(){
                console.log('clicked')
                const photo=document.querySelector(".photo")
                const url=photo.getAttribute("src")
                const scrollFromTop=document.body.scrollTop+10
                
                this.$store.state.url=url
                const zoom=document.querySelector(".zoomIn")
                const img=zoom.querySelector("img")
                img.style.top=window.scrollY+"px"
                img.setAttribute("src",url)
                zoom.style.display='block'
                console.log(img.style.top)
            },
            changeButtonColor(e){
                const targetBtn=e.target
                const nextEl=targetBtn.nextElementSibling   
                const preEl=targetBtn.previousElementSibling   
                            
                if(nextEl!=null)
                {
                    
                    nextEl.style.border="2px solid black"
                    nextEl.style.color="black"
                }
                else if(preEl!=null){
                    
                    preEl.style.border="2px solid black"
                    preEl.style.color="black"
                }
                targetBtn.style.border="2px solid orangered"
                targetBtn.style.color='orangered'
            },
            changePacketType(e){
                this.packetType=e.target.innerText
            },
            chageneSendWay(e){
                this.sendWay=e.target.innerText
            },
            changePayWay(e){
                
                this.payWay=e.target.innerText

            }
        }
    }
</script>


<style scoped>
    .writeAbleSignleItemTitle{
        width:50%
    }
    .writeAbleDetaileWrapper{
        display:flex;
        flex-direction:column;
        align-items: flex-end;
    }
    .writeAbleSignleItemBtns{
        margin-right:10px;
        width:50%;
        display:flex;
        justify-content: flex-end;
    }
    .writeAbleSignleItemBtns button{
        width:80px;
        margin:10px
    }
    .writeAbleSignleItem{
        display:flex;
        align-items: center;
        margin-top:20px;
        width:100%
    }
    .selectAbleBtns:focus{
        outline:none
    }
    .selectAbleBtns{
        background: white;
        padding:10px;
        border:2px solid black;
        font-size:13pt;
        font-weight: 600;
        transition: all 0.2s linear;
        color:black
    }
    #productDetail{
        border-bottom:1px solid rgb(199,199,199);
    }
    .productImg img{
        height: 290px;
        width: 290px;
        box-shadow:2px 2px 50px grey
    }
    .productImg{
        display:flex;
        /* height: 400px; */
        justify-content: flex-start;
        flex-direction:column;
    }
    .productImg div{
        display: flex;
        align-items: flex-end;
        justify-content: center;
        

    }
    .zoomSign{
        cursor: pointer;
    }
    .productImg div p{
        font-size: 14px;
        font-family: serif;
    }
    .productImg div img{
        max-width:15px;
        max-height:15px;
        margin-top:5px;
        margin-right: 5px;
    }
    .prodcuctName{
        text-align:left;
        width:100%;
    }
    .prodcuctName p{
        width:100%;
        text-align:right;
        padding-bottom: 10px;
        font-size:15pt
    }
    .productDetailWrapper{
        display:flex;
        
        padding:20px;
        flex-direction:column;
        justify-content: flex-start;
    }
    .productDetail{
        width:100%;
        display: flex;
        flex-direction:column;
        align-items: flex-start;
    }
    .productSingleDetailWrapper{
        width:100%;
        display:flex;
        flex-direction: column;
    }
    .justReadableDetailWrapper{
        width:100%;
        display:flex;
        flex-direction: column;
        align-items: center;

    }
    .productDetails{
        display:flex;
        justify-content:flex-start
    }
    .productDetailsWrap
    {
        display: flex;
        justify-content: flex-start;
        width:100%
    }
    .singleDetail{
        display:flex;
        width:100%;
        justify-content: flex-start;
        margin-top:10px;
    }
    .singleDetail p{
        max-width: max-content;
    }
    .order1{
        order:2;
        display: flex;
        justify-content: flex-end;
    }
    .order2{
        order:1;
        display: flex;
        justify-content: flex-end;
        word-wrap: break-word;
    }
    .singleDetail div{
        width:50%
    }
    .singleDetail{
        padding:10px;
        margin-left:5px;
        
    }
    .productSingleDetailWrapper .singleDetail:nth-child(odd){
        background:rgb(220,220,231)
    }
    .rating{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .rating div:nth-child(1)
    {
        margin-top:5px;
        
    }
    .rating{
        width:90%
    }
    .rating div:nth-child(2)
    {
        margin-top:5px;
    }
    .point p{
        font-size: 20pt;
    }
    .numbers{
        margin-top:20px;
    }
    .numbers p{
        font-size:18pt !important
    }
    .numbers span{
        color:rgb(240, 48, 48)
    }
    @media (max-width:650px)
    {
        .writeAbleSignleItem{
            flex-direction:column
        }
        .writeAbleSignleItemTitle{
            width:100%;
            order:1
        }
        .writeAbleSignleItemBtns{
            width:100%;
            order:2
        }
    }
    @media (min-width:320px) and (max-width:800px)
    {
        .productDetailsWrap{
            flex-direction:column
        }
        .productImg{
            display:flex;
            align-items: center;
        }
    
    }

</style>