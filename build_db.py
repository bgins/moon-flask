# The db needs to be created manually for now. Here are the commands.

# imports
from app import db, views
from app.views import User, Page, Post, SocialIcon

# create db
db.create_all()

# users
user_moon = User(username="Moon Flask", 
				 about="Moon Flask is a simple content management system built \
				 on Flask. You can use it to build a portfolio or personal \
				 website. Paolo Uccello serves as our sample user. Take a \
				 look at his interests below.")

# pages
dragons_page = Page(name="Dragons", 
					description="St. George in his famed battle against the Dragon.", 
					image=True, 
					author=user_moon)
hermits_page = Page(name="Hermits", 
					description="Early Renaissance monastic life.", 
					image=True, 
					author=user_moon)
polyhedra_page = Page(name="Polyhedra", 
					  description="My stellated dodecahedron and more.", 
					  image=True, 
					  author=user_moon)

# posts
dragons_post = Post(title="Dragons in our Times.", 
					body="Lorem ipsum dolor sit amet, consectetur adipiscing \
					elit. Ut et eros ante. Pellentesque tempor posuere diam \
					eget vulputate. Maecenas dignissim leo turpis, quis \
					vestibulum tortor pulvinar eget. Maecenas nec turpis ex. \
					Integer eu porta mauris, at consequat augue. Aliquam \
					posuere tincidunt nunc non mattis. Duis at urna sit amet \
					mi pharetra tincidunt. Phasellus diam massa, finibus nec \
					vulputate sed, molestie nec leo. Morbi ultricies consequat \
					odio, sed pulvinar ex vestibulum eu. Etiam cursus ornare \
					lacus, non hendrerit sem ultricies non. Morbi eget \
					placerat felis, ac blandit urna.",
					image=False,
					author=user_moon, 
					page=dragons_page)
stgeorge_post = Post(title="St. George and the Dragon", 
					 body="Pellentesque sed erat erat. Donec lacus purus, \
					 fermentum ut urna vitae, pretium varius orci. Aliquam \
					 ultrices dolor ut iaculis accumsan. Praesent quis pretium \
					 dolor. Phasellus eget faucibus metus. In hac habitasse \
					 platea dictumst. Donec ut diam eros. Aenean convallis \
					 orci eu feugiat vestibulum. In et facilisis lorem. Class \
					 aptent taciti sociosqu ad litora torquent per conubia \
					 nostra, per inceptos himenaeos. Suspendisse potenti. \
					 Vivamus commodo vulputate neque at posuere. Quisque \
					 laoreet pulvinar massa, id varius quam efficitur ut. \
					 Phasellus ultricies magna eu aliquam convallis.", 
					 image=True, 
					 author=user_moon, 
					 page=dragons_page)
hermits_post = Post(title="Episodes of the Hermit Life", 
					body="Pellentesque sed erat erat. Donec lacus purus, \
					fermentum ut urna vitae, pretium varius orci. Aliquam \
					ultrices dolor ut iaculis accumsan. Praesent quis pretium \
					dolor. Phasellus eget faucibus metus. In hac habitasse \
					platea dictumst. Donec ut diam eros. Aenean convallis orci \
					eu feugiat vestibulum. In et facilisis lorem. Class aptent \
					taciti sociosqu ad litora torquent per conubia nostra, per \
					inceptos himenaeos. Suspendisse potenti. Vivamus commodo \
					vulputate neque at posuere. Quisque laoreet pulvinar massa, \
					id varius quam efficitur ut. Phasellus ultricies magna eu \
					aliquam convallis.", 
					image=True, 
					author=user_moon, 
					page=hermits_page)
sketch_post = Post(title="Perspective Study of Mazzocchio", 
				   body="Integer elementum nulla ut erat dapibus euismod. \
				   Mauris ut libero sit amet risus aliquam gravida. \
				   Suspendisse in porta leo. Maecenas vitae porttitor nulla. \
				   Suspendisse luctus laoreet sollicitudin. Curabitur \
				   vestibulum dui ut luctus auctor. Quisque eget mi vitae nibh \
				   tincidunt rutrum. Pellentesque ac odio euismod, maximus \
				   nulla sit amet, eleifend erat. Vivamus nec consectetur \
				   turpis, ac mattis tortor.", 
				   image=True, 
				   author=user_moon, 
				   page=polyhedra_page)
shapes_post = Post(title="More Shapes", 
				   body="Mauris metus nisl, lobortis quis ex sed, dignissim \
				   eleifend libero. In ullamcorper id libero vel fermentum. \
				   Sed hendrerit nisl at dolor laoreet, quis mollis quam \
				   dictum. Etiam nec ipsum neque. Maecenas posuere lectus nec \
				   bibendum ultrices. Cras vehicula pellentesque purus vitae \
				   consequat. Duis ut mi blandit, mollis eros a, molestie \
				   lectus. Cras auctor felis ipsum, accumsan efficitur tortor \
				   semper sit amet. Nullam nec ex at odio molestie ullamcorper \
				   fringilla eu enim. Curabitur sollicitudin a lacus vel \
				   interdum. Nulla facilisi. Sed eleifend pulvinar leo, et \
				   mollis risus mollis in.",
				   image=False, 
				   author=user_moon, 
				   page=polyhedra_page)
embed_post = Post(title="Embed in an Iframe", 
				  body="Paolo does not have any work to embed. This post shows \
				  you can add an embed in place of an image.",
				  image=False, 
				  embed='<iframe width="100%" height="166" scrolling="no" \
				  frameborder="no" \
				  src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/44855438&amp;\
				  auto_play=false&amp;hide_related=false&amp;\
				  show_comments=true&amp;show_user=true&amp;\
				  show_reposts=false&amp;visual=true"></iframe>', 
				  author=user_moon, 
				  page=polyhedra_page)

# social icons
deviant_art_icon = SocialIcon(href="deviantart.com", 
							  css_value="fa fa-deviantart fa-lg", 
							  user=user_moon)
twitter_icon = SocialIcon(href="twitter.com", 
						  css_value="fa fa-twitter fa-lg", 
						  user=user_moon)
github_icon = SocialIcon(href="github.com", 
						 css_value="fa fa-github-alt fa-lg", 
						 user=user_moon)

# add to session
db.session.add_all([user_moon, dragons_page, hermits_page, polyhedra_page,
				    dragons_post, stgeorge_post, hermits_post, sketch_post,
				    shapes_post, embed_post, deviant_art_icon, twitter_icon,
				    github_icon])

# commit
db.session.commit()
print('Database build completed.')