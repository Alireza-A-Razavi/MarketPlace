<template>
  <div class="componyName profileRow">
    <div class="profileLabel componyNameLabel">
      <label class="need" for>زمینه های کاری شرکت</label>
    </div>
    <div class="componyWordFileds profileInput">
        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>صادرات</label>
            </div>
        </div>

        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>واردات</label>
            </div>
        </div>

        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>تولید</label>
            </div>
        </div>

        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>عرضه</label>
            </div>
        </div>


        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>صادرات</label>
            </div>
        </div>
        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>فلان</label>
            </div>
        </div>
        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>2فلان</label>
            </div>
        </div>

        <div class="pretty p-icon p-jelly p-round p-bigger singleCheckBox">
            <input type="checkbox" />
            <div class="state p-info">
                <i class="icon material-icons"></i>
                <label>3فلان</label>
            </div>
        </div>


    </div>
  </div>
</template>

<style scoped>
    .singleCheckBox{
        width:25%;
        margin-top:30px
    }
    .componyWordFileds{
        display:flex;
        flex-wrap: wrap;
    }
    @media (max-width:480px)
    {
        .componyWordFileds{
            flex-direction:column;
            align-items:flex-end
        }
    }
</style>

<script>
    export default{
        mounted()
        {
            // const singled=document.querySelectorAll(".singleCheckBox")
            // if(window.innerWidth>768)
            // {
                
            //     singled.forEach((sing,i)=>{
            //         if(i>=3){
            //             sing.style.marginTop="20px"
            //         }
            //     })
            // }else{
            //     singled.forEach((sing,i)=>{
            //         if(i>=3){
            //             sing.style.marginTop="20px"
            //         }
            //     })
            // }
        }
    }
</script>