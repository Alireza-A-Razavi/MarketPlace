<template>
	<div id="footer">
		<svg style="display:block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#0099ff" fill-opacity="1" d="M0,160L48,144C96,128,192,96,288,69.3C384,43,480,21,576,48C672,75,768,149,864,176C960,203,1056,181,1152,154.7C1248,128,1344,96,1392,80L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>
		<div id="footerWrapper">
			<div class="newsTake">
				<form>
					<p>برای دریافت اخرین قیمت ها ایمیل خود را وارد کنید</p>
					<input autocomplete="off" type="text" name="email">
					<button class='submit'>ثبت</button>
				</form>
			</div>
			<div class="aboutUs">
				<a href="#">در باره  ما</a>
			</div>
			<div class="phoneNum">
				<p>جهت دریافت اطلاعات با مما تماس بگیرید:</p>
				<p>021-35791862</p>
			</div>
		</div>
	</div>

</template>


<style scoped>
	svg{
		transform: rotate(180deg);
		position: relative;
    	top: -5px;
		width:100%;
		display:block
	}
	path{
		fill:#ffffff;
	}
	input{
		background: #201c29;	
		padding:5px;
		border:0;
		border-radius:10px;
		direction: ltr;
		color:white
	}
	input:-webkit-autofill {
		background-color: #201c29 !important;
		color: white !important;
	}
	#footerWrapper{
		display: flex;
		width: 95%;
		padding:20px;

		justify-content: space-between;
	}
	form input,form button
	{
		margin-top: 10px;
	}
	#footer{
		display: flex;
		flex-direction: column;
		align-items: center;
		background: rgb(16,14,23);
		/* position: relative; */
	}
	#footer p,#footer a{
		color:white
	}
	form{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.phoneNum p{
		text-align:center
	}
	@media (max-width: 1120px)
	{
		#footerWrapper{
			display: flex;
			flex-direction: column;
			align-items: center;
		}
		form p{
			text-align: center;
		}
		#footerWrapper > div{
			margin-top: 20px;
		}
	}

</style>


<script>
	
	export default{

	}
</script>