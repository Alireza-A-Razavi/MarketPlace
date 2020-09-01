<template>
    <div id="productComments">
        <div class="" id="productCommentsWrapper">
            <div class="sectionT">
                <div class="title">

                </div>
            </div>
            <div id="createNewComment">
                <div id="createNewCommentWrapper">
                        <form action="">
                            <textarea placeholder="نظر خد را بنویسید"></textarea>
                            <button type='submit' class='submit'>ثبت نظر</button>
                        </form>
                </div>
            </div>
            <div id="allComments">
                <div id="allComentsWrapper">
                    <div class="singleComment">
                        <div class="singleCommentWrap">
                            <div class="writerDetail">
                                <div class="date">
                                    <p>تاریخ:16/6/1399</p>
                                </div>
                                <div class="name">
                                    <p>عرفان شفیعی</p>
                                </div>
                                
                            </div>
                            <div class="comment">
                                <p>خوبه خوبه خوبه خوبه خوبه خوبه خوبه خوبه خوبه خوبه خوبه خوبه خوبه خومبه خوبننئنjjjjjjjjjjjjjjjjjjjjئنئنئنئنئنئنئه خوبه خوبه خوبه خوبه خوبه خوبه خوبه خیلی خوبه من دارمش عالیه خوبه خوبه </p>
                            </div>
                        </div>
                    </div>

                    <div class="commentSlicer">
                        <div></div>
                    </div>


                    <div class="singleComment">
                        <div class="singleCommentWrap">
                            <div class="writerDetail">
                                <div class="date">
                                    <p>تاریخ:16/6/1399</p>
                                </div>
                                <div class="name">
                                    <p>عرفان شفیعی</p>
                                </div>
                                
                            </div>
                            <div class="comment">
                                <p>خوبه</p>
                            </div>
                        </div>
                    </div>




                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
    .commentSlicer div {
        width: 75%;
        height:2px;
        background: rgb(172,172,172);
    }
    .commentSlicer{
        display: flex;
        justify-content: center;
    }
    #productComments{
        margin-top:50px;
    }
    #createNewCommentWrapper{
        display: flex;
        justify-content: center;
    }
    form{
        display: flex;
        flex-direction: column;
        align-items: center;
        width:100%
    }
    form button{
        margin-top:10px;
    }
    textarea{
        width:80%;
        height: 150px;
        direction: rtl;
        text-align: right;
        resize: none;
        font-size:15pt;
        padding:5px;
        
    }
    .singleCommentWrap{
        padding:20px;
        padding-right: 0;
    }
    .writerDetail{
        display: flex;
        justify-content: flex-end;
    }
    .writerDetail div:nth-child(1)
    {
        margin-right:20px
    }
    #allComentsWrapper .singleComment:not(first-child)
    {
        margin-top:30px
    }
    #allComentsWrapper{
        display: flex;
        flex-direction:column;
        width:95%
    }
    .comment p{
        max-width:400px;
        /* word-break: break-all; */
        word-wrap: break-word;
        text-align: justify;
    }
    .comment{
        display:flex;
        justify-content: flex-end;
        margin-top:10px;
    }
    .name p{
        color:#ff2654
    }
    @media (min-width:320px) and (max-width: 362px)
    {
        .name p,.date p{
            font-size:13pt
        }
        .singleCommentWrap{
            padding:0;
        }
        .comment p{
            max-width:95%;
        }
        .commentSlicer{
            display: flex;
            margin-top:10px;
            /* margin-bottom:10px; */
            justify-content: center;
        }
        #allComentsWrapper .singleComment:not(first-child)
        {
            padding-bottom:10px
        }   
    }

</style>


<style>


</style>