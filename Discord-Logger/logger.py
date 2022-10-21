from discord_webhook import DiscordWebhook, DiscordEmbed

nuke = raw data for "\\nuker"

config = "./config.json"

webhook = DiscordWebhook(url=config.webhook_url)



embed = DiscordEmbed(title=config.webhook_title_url, description=nuke.informations, color=config.webhook_color_url)

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()
