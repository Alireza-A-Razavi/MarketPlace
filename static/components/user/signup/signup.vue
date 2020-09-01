<template>
    <div id="signup">
        <div id="signupWrapper" v-if='signupFormShouldShowMethod()'>
            <div class="title">
                <p>ثبت نام</p>
            </div>
            <div id="signupForm">
                <form action="">
                    <div id="email" class="inputs">
                        <div class='formInputsWrapper'>
                                
                                <input @blur='focusOut' id='userEmail' type="text">
                                <label for="userEmail">ایمیل</label>

                        </div>
                    </div>
                    <div id="password" class="inputs">
                        <div class='formInputsWrapper'>
                                
                                <input @blur='focusOut' id='userPassword' type="text">
                                <label for="userPassword">رمز</label>
                        </div>
                    </div>
                    <div id="passwordConf" class="inputs">
                        <div class='formInputsWrapper'>
                                 
                                <input @blur='focusOut' id='userPasswordCond' name='passConf'  type="text">
                                <label for="userPasswordCond">تایید رمز</label>
                        </div>
                    </div>
                    <div id="submit" class='inputs'>
                        <button class="submit">
                            ثبت نام
                        </button>
                    </div>
                </form>
            </div>
        </div>





        <div id="signupWrapper" v-if='signinFormShouldShowMethod()'>
            <div class="title">
                <p>ورود</p>
            </div>
            <div id="signupForm">
                <form action="">
                    <div id="email" class="inputs">
                        <div class='formInputsWrapper'>
                                
                                <input @blur='focusOut' id='userEmail' type="text">
                                <label for="userEmail">ایمیل یا نام کاربری</label>

                        </div>
                    </div>
                    <div id="password" class="inputs">
                        <div class='formInputsWrapper'>
                                
                                <input @blur='focusOut' id='userPassword' type="text">
                                <label for="userPassword">رمز</label>
                        </div>
                    </div>
                    <div id="submit" class='inputs'>
                        <button class="submit">
                            ورود
                        </button>
                    </div>
                </form>
            </div>
        </div>




    </div>

</template>

<style scoped>
    #signup{
        background: white;
        margin-top:20px;
        border-radius: 5px;
        border:1px solid rgb(180,180,180)
    }
    label,p{
        color:rgb(41,41,41)
    }
    #signupWrapper{
        display:flex;
        flex-direction:column;
        justify-content: center;
        padding:10px        
    }
    form{
        width:100%;
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .inputs{
        display: flex;
        justify-content: space-evenly;
        width:100%;
        margin-top:20px;
    }
    .formInputsWrapper{
        width:max-content;
        display: flex;
        justify-content: center;
        align-items:center;
        position: relative;
    }
    form div div{
        display:flex;
        justify-content: space-around;
    }
    input + label{
      display:block;
        cursor:text;
        color:#777;
        transition:.15s ease-out all;
        position:absolute;
        right:1em;
    }
    .title{
        display:flex;
        justify-content: center;
        font-size:24pt
    }
    input{
        border:1px solid rgb(180,180,180);
        border-radius:5px;
        padding:1em 1em .8em 1em;
        color:black
    }
    input:focus + label,
    label.stay
    {
        animation:changeLabel 0.5s linear;
        position:absolute;
        top:2px;
        color:#139dd7;
        font-size:12pt
    }

</style>


<script>
    export default{
        mounted(){
            const inputs=document.querySelectorAll(".formInputsWrapper input")
            inputs.forEach(inp=>{
                inp.addEventListener("focus",input=>{
                
            })
            })
            console.log(inputs)
        },
        props:["signupformshouldshow",'signinformhouldshow'],


        methods:{
            focusOut(e){
                const input=e.target
                const label=input.nextElementSibling
                if(input.value!='')
                {
                    label.classList.add("stay")
                    return
                }
                label.classList.remove("stay")
            },
            signupFormShouldShowMethod(){
                return this.signupformshouldshow=="true" ? true : false
            },
            signinFormShouldShowMethod(){
                return this.signinformhouldshow=="true" ? true : false
            }
        }
    }
</script>