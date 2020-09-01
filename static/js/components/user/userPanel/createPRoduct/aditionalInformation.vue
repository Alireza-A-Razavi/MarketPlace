<template>
  <div id="aditionalInformation" class="productSection">
    <div class="aditionalInformationWrapper">
      <div class="title">
        <p>اطلاعات اضافی</p>
      </div>
      <div class="information">
        <div class="informationWrapper">
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>حداکثر سفارش</label>
              </div>
              <div class="col1Input">
                <input type="text" placeholder="حداکثر تعداد" />
              </div>
            </div>

            <div class="col2">
              <div class="col2Label">
                <label for>حداقل سفارش</label>
              </div>
              <div class="col2Input">
                <input type="text" placeholder="حداقل تعداد" />
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <p></p>
                <label for>رنگ</label>
              </div>
              <div class="col1Input">
                <input type="text" placeholder="با فاصله جدا شود" />
              </div>
            </div>

            <div class="col2">
              <div class="col2Label">
                <label for>وزن</label>
              </div>
              <div class="col2Input">
                <input type="text" placeholder="وزن" />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>کشور ساخت</label>
              </div>
              <div class="col1Input">
                <input type="text" placeholder="کشور ساخت" />
              </div>
            </div>

            <div class="col2">
              <div class="col2Label">
                <label for>قیمت</label>
              </div>
              <div class="col2Input">
                <input type="text" placeholder="قیمت" />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>جنس</label>
              </div>
              <div class="col1Input">
                <input type="text" placeholder="جنس" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>




<style scoped>
  label::after{
    content:' *';
    color:red;
    font-size:20pt;
    font-weight: 900;
  } 
    .title p{
        color:#0061af;
        font-size:17pt;
        font-weight: lighter;
    }
    input{
            color:black;
            direction:rtl;
            border:1px solid rgb(210,214,222);
            padding:10px
        }
    .col1Label,.col2Label,.col1Input,.col2Input{
        width:50% 
    }
    .col1Input input,.col2Input input{
        width:250px
    }
    .row{
        width:100%;
        display:flex;
        margin-top:20px;
        justify-content: flex-start;
    }
    .col1,.col2{
        width:50%;
        display:flex;
        justify-content: center;
        align-items: center;
    }
    .informationWrapper{
        margin-right:30px;
    }
    .information{
        margin-top:20px;
        margin-bottom:20px
    }
    .col1Label,.col2Label{
        display:flex;
        justify-content: flex-end;
        margin-right:10px
    }
    .col1Input,.col2Input{
        display:flex;
        justify-content: flex-end;
    }

  @media (max-width:880px)
  {
    .row{
      flex-direction:column
    }
    .col1,.col2{
      display:flex;
      width:100%;
      flex-direction:column
    }
    .col1 .col1Label,.col2 .col2Label,.col1 .col1Input,.col2 .col2Input{
      width:100%
    }
    .col1 .col1Label,.col2 .col2Label{
      margin-top:10px;
      margin-bottom:10px
    }
    .col1Input input,.col2Input input{
      width: 90%;
    }
    label::after{
    content:'';
    color:red;
    font-size:20pt;
    font-weight: 900;
  } 
  label::before{
    content:'* ';
    color:red;
    font-size:20pt;
    font-weight: 900;
  }
  }
</style>