<template>
    <div class="zoomIn" @click='closeZoomIn'>
        <img @click='prevent' src="" alt="">
    </div>
</template>

<script>
    export default{
        methods:{
            closeZoomIn(){
                const zoomIn=document.querySelector(".zoomIn")
                zoomIn.style.display="none"
                document.body.style.overflowY=''
            },
            prevent(e){
                e.stopPropagation();
                
            }
            
        }
    }
</script>

<style scoped>
    .zoomIn{
        position: absolute;
        display: none;
        width: 100%;
        height: 100%;
        overflow: auto;
        z-index:554;
        background: rgba(0,0,0,0.8);
        transition: all 1s linear;
    }
    .zoomIn img{
        position: absolute;
        z-index:555;
        max-width:100%;
        max-height: 700px;
        left: 50%;
        margin-top:100px;
        transform: translateX(-50%);
        display: block;
        
    }
</style>