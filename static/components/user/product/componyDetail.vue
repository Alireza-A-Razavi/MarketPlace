<template>
    <div id="componyDetail">
        <table>
            <tbody>
                <tr>
                    <th>سال تاسیس کمپانی:</th>
                    <td>1375</td>
                    
                    
                </tr>
                <tr>
                    <th>محل شرکت:</th>
                    <td>تهران</td>
                    
                    
                </tr>
                <tr>
                    <th>دسته بندی محصول:</th>
                    <td>صوتی</td>
                    
                    
                </tr>
                <tr>
                    <th>تعداد کارمندان:</th>
                    <td>30 تا 40 نفر</td>
                
                </tr>
            </tbody>
        </table>
    </div>
    
</template>

<style scoped>
#componyDetail{
    display:flex;
    justify-content: center;
}
    table{
        width: 95%;
        max-width: 100%;
        margin-bottom: 20px;
    }
    td{
        text-align:left;
        width:50%
    }
    td,th{
        padding:10px
    }
    tr{
        border-top:1px solid rgb(191, 202, 202)
    }
    tr:nth-child(odd):hover{
        background: rgb(221, 215, 215);
    }
    th{
        text-align:left;
        width:50%
    }
</style>