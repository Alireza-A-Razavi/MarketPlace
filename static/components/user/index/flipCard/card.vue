<template>
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <img :src="getImg()" alt="Avatar" style="width:300px;height:300px;" />
        <p>{{title}}</p>
      </div>
      <div class="flip-card-back">
          <p>{{descs}}</p>
      </div>
    </div>
  </div>
</template>
<script>

        export default{
            props:["descs","img",'title'],
            methods:{
                getImg(){
                    return this.img
                }
            }
        }
</script>


<style scoped>
.flip-card-front img{
    width:50px !important;
    height:50px !important
}
.flip-card {
  background-color: transparent;
  min-width: 300px !important;
  height: 300px;
  margin-top:50px;
  padding:5px
  /* perspective: 1000px; */
  
}

.flip-card-inner {
  position: relative;
  width: 100%;
  border:1px solid rgb(216, 205, 205);
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  display:flex;
  flex-direction:column;
  align-items: center;
  justify-content: center;
}

.flip-card-front {
  background-color: rgb(56, 56, 56);
  color: white;
}

.flip-card-back {
  background-color: #2980b9;
  color: white;
  transform: rotateY(180deg);
}
.flip-card-back p{
    max-width: 80%;
    text-align: center;
}
</style>