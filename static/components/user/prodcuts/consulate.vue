<template>
    <div v-show='shoudIShow' id="consulate" @click='toggleConsulate(),changeBodyOverFlow()'>
        <div @click='prevent($event)' id="consulateWrapper">
            <div class="input">
                <label for="name">نام:</label>
                <input autocomplete="off" type="text" id='name' name="" placeholder="نام">
            </div>
            <div class="input">
                <label for="phone">شماره تلفن:</label>
                <input autocomplete="off" type="text" id='phone' name="" placeholder="شماره تلفن">
            </div>
            <div>
                <button @click='consulateRequest()' class="submit">ثبت</button>
            </div>

        </div>
    </div>

</template>

<script>
    import {mapActions} from 'vuex'
    
    export default {
        methods:{
            ...mapActions([
                'toggleConsulate'
            ]),
            prevent(e){
                e.preventDefault();
                e.stopPropagation()
            },
            changeBodyOverFlow(){
                document.body.style.overflow=''
            },
            consulateRequest(){
                const doneMessage=document.querySelector('#doneMessage')
                doneMessage.style.display='block'
                this.toggleConsulate()
                this.changeBodyOverFlow()
                setTimeout(()=>{
                    doneMessage.style.display='none'
                },5000)
            }
        },
        computed:{
            shoudIShow(){
                return this.$store.state.isShowConsulate
            }            
        }        
    }
</script>

<style scoped>
    #consulate{
        position: absolute;
        width:100%;
        height:100%;
        display:none;
        top:0;
        right:0;
        left:0;
        bottom:0;
        display: flex;
        background: rgb(0,0,0,0.6);
        z-index:666;
        transition: all 0.3s;
        animation: fadeIn 0.3s linear;
    }
    @keyframes fadeIn {
        from{
            opacity: 0;
        }
        to{
            opacity: 1;
        }
    }
    #consulateWrapper{
        display: flex;
        flex-direction: column;
        align-items: center;
        position:absolute;
        background: rgb(233, 233, 233);
        padding:20px;
        left:50%;
        transform: translateX(-50%);
    }
    .submit{
        margin-top:20px;
    }
    .input{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .input label,.input input{
        padding:10px;
        color:black;

    }
    .input:nth-child(:first-child) input
    {
        direction: rtl;
    }
    .input:nth-child(2) input
    {
        direction: ltr;
    }
</style>
