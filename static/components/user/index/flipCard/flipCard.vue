<template>
    <div id="fliped">
        <card
            title="تضمین کیفیت"
            img="/images/cup.png"
            descs="تضمین کیفیت تمامی محصولات"
        ></card>
        <card 
            title="گارانتی تضمینی"
            img="/images/shield.png"
            descs="گارانتی تمام محصولا 10 ساله"
        ></card>
        <card
            title="گارانتی تضمینی"
            img="/images/shield.png"
            descs="گارانتی تمام محصولا 10 ساله"
        ></card>
        <card
            title="گارانتی تضمینی"
            img="/images/cup.png"
            descs="گارانتی تمام محصولا 10 ساله"
        ></card>
        <card 
            title="گارانتی تضمینی"
            img="/images/cup.png"
            descs="گارانتی تمام محصولا 10 ساله"
        ></card>
        <card
            title="گارانتی تضمینی"
            img="/images/shield.png"
            descs="گارانتی تمام محصولا 10 ساله"
        ></card>
    </div>

</template>

<script>
    import card from './card.vue'

    export default{
        components:{
            card
        }
    }
</script>

<style scoped>
    #fliped{
        max-width:900px;
        display:flex;
        justify-content: center;
        flex-wrap: wrap;
        margin-top:50px;
    }
</style>