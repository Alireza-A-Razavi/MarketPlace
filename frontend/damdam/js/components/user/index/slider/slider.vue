<template>
	<div id="slider">
		<div id="sliderWrapper">
			<div class="active slide">
				<img src="/images/ec1.png" alt="">
				<div class="container">
					<div class="containerWrapper">
						<p>شرینگ پک</p>
						<!-- <p>انواع شرینگ پک فلان فلان فلانف فلان</p> -->
						<button class='submit'>مشاهده</button>
					</div>
				</div>
			</div>
			<div class="slide">
				<img src="/images/ec2.png" alt="">
				<div class="container">
					<div class="containerWrapper">
						<p>شرینگ پک</p>
						<!-- <p>انواع شرینگ پک فلان فلان فلانف فلان</p> -->
						<button class='submit'>مشاهده</button>
					</div>
				</div>
			</div>
		</div>
		<div class="controlls">
			<div class="pre" @click="pre()"><</div>
			<div class="next" @click='next()'>></div>
		</div>
	</div>
</template>

<script>
	export default {
		mounted(){
			this.slides=document.querySelectorAll(".slide")
		},
		data(){
			return{
				slides:null,
				index:0,
				isMount:false
			}
		},
		methods:{
			pre(){
				if(this.index==0)
				{
					this.index=this.slides.length-1
				}else{
					this.index--
				}
				this.changeSlide()
			},
			next(){
				if(this.index==this.slides.length-1)
				{
					this.index=0
				}else{
					this.index++
				}
				this.changeSlide()
			},
			changeSlide(){
				for(let i=0;i<this.slides.length;i++){
					this.slides[i].classList.remove("active")
				}
				this.slides[this.index].classList.add("active")
			},
			
			
		},
	}	
</script>

<style scoped>
	.controlls .pre,.controlls .next{
		position: absolute;
		top:50%;
		height:40px;
		width:40px;
		cursor:pointer;
		z-index:2;
		color:#000000;
		background-color: rgba(255, 153, 0, 0.4);
		text-align:center;
		line-height: 40px;
		transition:all 0.5s ease;
		font-size: 20pt;
		font-weight: 700;
	}
	.next{
		right:0
	}
	
	img{
		width:100%
	}
	#sliderWrapper{
		display:flex;
		justify-content: center;
		overflow: hidden;
	}
	.slide{
		position: relative;
		
		display:none;
		animation: slide 2s ease;
	}
	.slide,#slider{
		max-height: max-content;
	}
	#slider{
		position:relative;
		width:688px;
		max-height:max-content
	}
	.container{
		position:absolute;
		top:50%;
		left:50%;
		transform:translateX(-50%) translateY(-50%)
		
	}
	.containerWrapper{
		display:flex;
		flex-direction:column;
		align-items: center;
		padding:20px
	}
	.container p{
		font-size:18pt;
		font-weight: lighter;
		
	}
	.slide.active p{
		opacity:0;
		animation:captionTextAn 0.5s linear forwards;
		animation-delay: 1.2s;
		color:white;
		margin-bottom:10px
	}
	.slide.active .container{
		animation:fadeTrans 1s linear forwards;
		animation-delay: 1.5s;
	}
	@keyframes fadeTrans {
		0%{
			background: transparent;
		}
		100%{
			background: rgba(0, 0, 0, 0.7);
		}
	}
	.slide.active button{
		opacity:0;
		animation:captionTextAn 0.5s linear forwards;
		animation-delay: 1.4s;
	}
	@keyframes captionTextAn{
		from {
			opacity:0;
			transform:translateX(-100px)
		}
		to{
			opacity:1;
			transform:translateX(0px)

		}
	}

	
	.slide.active{
		display:flex
	}
	.container p:nth-child(2){
			font-size:12pt
		}
	@keyframes slide{
		0%{
			opacity:0;
			transform: scale(1.2);
		}
		100%{
			opacity:1;
			transform:scale(1)
		}
	}
	@media (max-width:650px){
		.container p,.container button{
			font-size:12pt;
			font-weight: lighter;
		}
	}
	@media (max-width:924px)
	{
		#slider{
			width:100%;
			
		}
		img{
			object-fit: contain;
			height:auto;
		}
	}
</style>