<template>
    <div class="componyBriefIntroduction profileRow">
        <div class="profileLabel componyBriefIntroductionLabel">
              <label class='need' for="">در باره شرکت</label>
         </div>
        <div class="componyBriefIntroductionInput profileInput">
            <textarea v-model='chars' name="briefIntroduction" maxlength="100" id="" cols="10" rows="8"></textarea>

            <p ><span>حداکثر تعداد کاراکتر</span>: <span>{{(100 - chars.length)}}</span></p>
        </div>
    </div>
</template>

<script>
export default{
    data(){
        return{
            chars:''
        }
    }
}

</script>

<style scoped>
    textarea{
        resize: none;
        direction: rtl;
    }
    .componyBriefIntroductionInput{
        display:flex;
        flex-direction:column;
        width:300px

    }
    .componyBriefIntroductionInput p span:nth-child(2){
        color:orangered;
        margin-top:10px
    }
    @media (max-width:768px)
    {
        .componyBriefIntroductionInput{
            width:100%
        }

    }
</style>