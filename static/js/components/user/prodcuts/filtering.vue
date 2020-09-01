<template>
    <div id="filtering" @click='checkelements($event)' v-if='shoudShow()'>
        <div id="filteringWrapper">



            <div id="filterByRegion">
                <div class="filteringTit">
                    <p>کشور تولید</p>
                </div>
                <div class="allRegions">
                    <div class="singleRegion">
                        <div class='regionCountry'>
                            <input type="checkbox" name="regions[]">
                        </div>
                        <div class="label">
                            <label for="">چین</label>
                        </div>
                        
                    </div>
                    <div class="singleRegion">
                        <div class='regionCountry'>
                            <input type="checkbox" name="regions[]">
                        </div>
                        <div class="label">
                            <label for="">کره</label>
                        </div>
                        
                    </div>
                    <div class="singleRegion">
                        <div class='regionCountry'>
                            <input type="checkbox" name="regions[]">
                        </div>
                        <div class="label">
                            <label for="">ایران</label>
                        </div>
                        
                    </div>
                    <div class="singleRegion">
                        <div class='regionCountry'>
                            <input type="checkbox" name="regions[]">
                        </div>
                        <div class="label">
                            <label for="">آلمان</label>
                        </div>
                        
                    </div>
                </div>
            </div>


            <hr>


            <div id="filteringByPrice">
                <div class="title">
                    <p>فیلتر با قیمت</p>
                </div>
                <div class="allPrices">
                    <div class="from">
                        <input @change="checkInput($event)" type="text" name='priceFrom' placeholder="قیمت از...">
                    </div>
                    <div class="to">
                        <input @change="checkInput($event)" type="text" name='priceFrom' placeholder="تا...">
                    </div>
                </div>

            </div>

            <hr>


            <div id="submitFiltering">
                <button class=submit>فیلتر</button>
            </div>



        </div>
    </div>
</template>


<style scoped>

    #filtering{
        display:flex;
        position: absolute;
        right:0;
        width:100%;
        height:100%;
        top:0;
        bottom:0;
        z-index:666;
        background: rgba(0,0,0,0.4);
    }
    #filteringWrapper{
        padding:10px;
        position:absolute;
        right:0;
        background:  rgb(20,40,80);
        height:100%;
        top:0;
        color:white
    }
    .singleRegion{
        display:flex;
        justify-content: space-between;
        margin-top:10px
    }
    .allRegions{
        display:flex;
        flex-direction: column;
    }
    .regionCountry{
        width:30%
    }
    .allPrices{
        margin-top:10px;

    }
    .filteringByPrice title{
        margin-top:10px
    }
    .from,.to{
        margin-top:10px;
        
    }
    .from input,.to input
    {
        color:black;
        border:0;
    }
    .from input:focus,.to input:focus{
        direction: ltr;
    }
    .forceLtr{
        direction:ltr
    }
    #submitFiltering{
        display:flex;
        justify-content: center;
    }
</style>



<script>
import {mapActions} from "vuex"
export default {
    methods:{
        ...mapActions([
            'toggleFiltering'
        ]),
        shoudShow(){
            return this.$store.state.isShowFiltering
        },
        checkelements(e){
            console.log(e.target.id)
            if(e.target.id=='filtering')
            {
                this.toggleFiltering()
            }
        },
        checkInput(e){
            if(e.target.value!='')
            {
                e.target.classList.add("forceLtr")
                return
            }
            e.target.classList.remove("forceLtr")
        }
    }
}
</script>