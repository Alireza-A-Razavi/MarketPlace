<template>
    <div id="createProduct" class='userPanelComp'>
        <div id="createProductWrapper">
            <form action="/testy" method="post">
                <select-category></select-category>
                <div id="name" class='productSection'>
                    <div id="nameWrapper">
                        <label for="">نام محصول:</label>
                        <input type="text" placeholder="نام" name='productName'>
                    </div>
                </div>
                <slicer></slicer>
                <product-img></product-img>
                
                <slicer></slicer>

                <product-descs></product-descs>

                
                <slicer></slicer>
                <aditional-information></aditional-information>
                <slicer></slicer>

                <button type='submit' class='submit'>
                    ثبت محصول
                </button>

                
            </form>
        </div>
    </div>
</template>

<style scoped>
    #nameWrapper label:before{
        content:' * ';
        color:red;
        font-size:20pt;
        font-weight:900
    }
    #aditionalInformation{
        padding:5px
    }
    form{
        width:100%
    }    
    #createProductWrapper{
        width:100%;
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    #createProductWrapper form{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    #slicer{
        margin-top:20px
    }    
    .productSection{
        margin-top:20px;
        width:100%;
        display:flex;
        flex-direction: column;
        justify-content: center;
    }
    
    #nameWrapper{
        display:flex;
        flex-direction:column;
        justify-content: center;
        align-items: center;
    }
    #nameWrapper input{
        width:200px
    }
    #nameWrapper label{
        margin-bottom:10px
    }
    
    input[type="text"]{
        color:black;
        
        width:30%;
        padding:10px;
    }
    input{
        border:1px solid rgb(210,214,222);
    }
        
    .orderInput input{
        width:100%
    }
    .submit{
        margin-top:20px;
        margin-bottom:20px;
    }

    .title p,#productDescsWrapper label{
        color:#0061af;
        font-size:17pt;
        font-weight: lighter;
    }
    @media (max-width:500px)
    {
        #nameWrapper{
            display:flex;
            flex-direction:column
        }
        #nameWrapper input{
            width:90%
        }
    }
    
</style>

<script>
    import slicer from '../../template/slicer/slicer.vue'
    import Editor from '@tinymce/tinymce-vue'
    import productImg from './productImg.vue'
    import productDescs from './productDescs.vue'
    import aditionalInformation from "./aditionalInformation.vue"
    import selectCategory from './selectCategory.vue'
    export default{
        methods:{
            
        },
        components: {
            editor: Editor,
            slicer,
            selectCategory,
            productImg,
            productDescs,
            aditionalInformation
        },
        
    }
</script>