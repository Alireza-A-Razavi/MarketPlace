<template>
    <div id="selectCategory">
        <div id="selectCategoryComponent">
            <label for="">دسته بندی محصول را انتخاب کنید</label>
            <input placeholder="جست و جو..." list="browsers" autocomplete="off" name="category">
            <datalist id="browsers">
                <option value="دسته 1"></option>
                <option value="دسته 2"></option>
                <option value="دسته 3"></option>
                <option value="دسته 4"></option>
                <option value="دسته 1"></option>
                <option value="دسته 2"></option>
                <option value="دسته 3"></option>
                <option value="دسته 4"></option>
                <option value="دسته 5"></option>
                <option value="دسته 1"></option>
                <option value="دسته 2"></option>
                <option value="دسته 3"></option>
                <option value="دسته 4"></option>
                <option value="دسته 5"></option>
                <option value="دسته 1"></option>
                <option value="دسته 2"></option>
                <option value="دسته 3"></option>
                <option value="دسته 4"></option>
                <option value="دسته 5"></option>
                <option value="دسته 1"></option>
                <option value="دسته 2"></option>
                <option value="دسته 3"></option>
                <option value="دسته 4"></option>
                <option value="دسته 5"></option>
                <option value="دسته 1"></option>
                <option value="دسته 2"></option>
                <option value="دسته 3"></option>
                <option value="دسته 4"></option>
                <option value="دسته 5"></option>
                <option value="دسته 1"></option>
                <option value="دسته 2"></option>
                <option value="دسته 3"></option>
                <option value="دسته 4"></option>
                <option value="دسته 5"></option>
                <option value="دسته 5"></option>
            </datalist>
        </div>
    </div>
</template>
<style scoped>
    input{
        color:black;
        direction:rtl;
        border:1px solid rgb(210,214,222);
        padding:10px
    }

    #selectCategory{
        margin-top:20px;
        margin-bottom:20px;
        width:100%
    }
    #selectCategoryComponent{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    label{
            margin-bottom:10px
        }
    label:before{
        content:"* ";
        color:red;
        font-size:20pt;
        font-weight: 900;
    }
    @media (max-width: 500px)
    {
        #selectCategoryComponent{
            display:flex;
            flex-direction:column;
            align-items: center;
        }
        
        #selectCategoryComponent input,#selectCategoryComponent datalist{
            width:90%
        }

    }
</style>

<script>
    // import vSelect from 'vue-select'
export default {
    components:{
        // vSelect
    },
    data(){
        return{
            options:['Canada', 'United States']
        }
    }
}
</script>