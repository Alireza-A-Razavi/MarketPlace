<template>
    <div id="profile" class='userPanelComp'>
        <div id="profileWrapper">
            <div class="title">
                <p>اطلااعات کمپانی
                    <i class='fa fa-building-o'></i>

                </p>
            </div>


            <div class="profile">


                <form action="">
                    <compony-name></compony-name>
                    <compony-website></compony-website>
                    <compony-work-fields></compony-work-fields>
                    <compony-brief-introduction></compony-brief-introduction>
                    <compony-workers-numbers></compony-workers-numbers>
                    <compony-year-stablished></compony-year-stablished>
                    <compony-map></compony-map>
                    <div class="updateProfile">
                        <button style="margin-top:20px" class='submit'>ویرایش پروفایل</button>
                    </div>
                </form>
            
            </div>
        </div>




    </div>

</template>


<script>

    import componyName from './componyName.vue'
    import componyWebsite from "./componyWebsite.vue"
    import componyWorkFields from './componyWorkFields.vue'
    import componyBriefIntroduction from "./componyBriefIntroduction.vue"
    import componyWorkersNumbers from './componyWorkersNumbers.vue'
    import componyYearStablished from './componyYearStablished.vue'
    import componyMap from "./componyMap.vue"
    export default{
        components:{
            componyName,
            componyWebsite,
            componyWorkFields,
            componyBriefIntroduction,
            componyWorkersNumbers,
            componyYearStablished,
            componyMap
        }
    }

</script>



<style>
    .updateProfile{
        display: flex;
        width: 100%;
        justify-content: center;
    }
    .profile{
        margin-top:20px
    }
    .profileInput{
        width:60%;
    }
    .profileRow{
        display:flex;
        margin-top:40px;
        align-items: flex-start;
    }
    .profileLabel{
        width:40%;
        display:flex;
        justify-content: flex-end;
    }
    .profileLabel label{
        margin-right:20px
    }
    #profileWrapper{
        padding:20px
    }
    .profileInput input{
        border:1px solid rgb(210,214,222);
        padding:5px;
        width:300px;
        color:black
    }
    select{
        width:300px;
        padding:5px;
        border:1px solid rgb(210,214,222);
        background-color: white;
        direction:rtl;
        font-size:15pt;
        font-weight: lighter;
    }
    textarea{
        border:1px solid rgb(210,214,222);
    }
    option{
        font-size:15pt;
        font-weight: lighter;
    }

    @media (max-width:768px)
    {
        .profileRow{
            flex-direction:column;

        }
        .profileRow .profileLabel{
            margin-top:10px;
            margin-bottom:10px
        }
        .profileLabel,.profileInput,.componyBriefIntroductionInput,.componyWordFileds{
            width:100%
        }
        .profileInput input,.profileInput select,.profileInput textarea,.profileInput select{
            width:100%
        }

    }

</style>