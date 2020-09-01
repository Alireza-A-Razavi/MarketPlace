<template>
    <div id="doneMessage">
        <div id="doneMessageWrapper">
            <img src="/images/check.png" alt="">
            <p>درخواست شما با موفقیت انجام</p>
        </div>
    </div>
</template>

<style scoped>
    #doneMessage{
        display:none;
        position: fixed;
        right:0;
        top:50px;
        background: rgb(176, 240, 179);
        color:black;
        border-radius: 5px;
        z-index: 666;
    }
    #doneMessageWrapper{
        display:flex;
        padding:20px;
        align-items: center;
    }
    p{
        font-size:12pt
    }
    img{
        width:40px;
        height:40px;
    }
    
</style>