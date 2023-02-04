from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(1656503707) # timespamp that was at the end before
        self.writeVInt(1995904808) # new timespamp
        self.writeVInt(2022180) # timestamp, Logic Daily Data begin
        self.writeVInt(72292) # timestamp
        self.writeVInt(player.Trophies) # current trophies
        self.writeVInt(player.HighestTrophies) # highest trophies
        self.writeVInt(player.HighestTrophies) # highest trophies 
        self.writeVInt(player.TrophyRoadTier) # collected trophy road rewards
        self.writeVInt(120000) # exp points
        self.writeDataReference(28, player.Thumbnail) # profile icon
        self.writeDataReference(43, player.Namecolor) # name color

        self.writeVInt(20) # played game mode count
        for x in range(20):
            self.writeVInt(x)

        self.writeVInt(0) # selected skin count

        self.writeVInt(0) # available ramdon skins

        self.writeVInt(0) # random skins

        self.writeVInt(630)
        for x in range(630):
            self.writeDataReference(29, x) # unlocked skin array

        self.writeVInt(0) # skin purchase option

        self.writeVInt(0) # unk skin array5

        self.writeVInt(0) # leaderboard region
        self.writeVInt(0) # highest trophies
        self.writeVInt(0) # tokens used in battle
        self.writeVInt(1) # control mode
        self.writeBoolean(True) # battle hints
        self.writeVInt(0) # token doubler left
        self.writeVInt(0) # trophy league timer
        self.writeVInt(0) # power play timer
        self.writeVInt(0) # Brawl pass season timer

        self.writeVInt(0) # 
        self.writeVInt(0) # 
        self.writeVInt(0) # drop chance of characters in boxes

        self.writeByte(1) # false, false, true
        self.writeVInt(2) # token doubler  new tag state
        self.writeVInt(2) # event tickets new tag state
        self.writeVInt(2) # coins pack new tag state
        self.writeVInt(0) # name change cost
        self.writeVInt(0) # timer for next name change

        self.writeVInt(1) # shop offer count

        self.writeVInt(1)  # RewardCount
        for i in range(1):
            self.writeVInt(40) # ItemType
            self.writeVInt(1)
            self.writeDataReference(16, 65) # CsvID
            self.writeVInt(1)

        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(950400)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(3917)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(49)
        self.writeInt(0)
        self.writeString("Offer")
        self.writeBoolean(False)
        self.writeString("offer_lastbox")
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(True)
        self.writeVInt(0)

        self.writeVInt(200) # tokens for battle
        self.writeVInt(-64) # timer for new token

        self.writeVInt(0) # count

        self.writeVInt(0) # unk
        self.writeVInt(0) # unk2

        self.writeVInt(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString('CA') # location
        self.writeString('BSDS')

        self.writeVInt(20)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # Tokens Gained
        self.writeLong(4, 0)  # Trophies Gained
        self.writeLong(6, 0)  # Demo Account
        self.writeLong(7, 0)  # Invites Blocked
        self.writeLong(8, 0)  # Star Points Gained
        self.writeLong(9, 0)  # Show Star Points
        self.writeLong(10, 0)  # Power Play Trophies Gained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # Coins Gained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 0)  # Team Chat Muted
        self.writeLong(18, 1)  # Esport Button
        self.writeLong(19, 0)  # Champion Ship Lives Buy Popup
        self.writeLong(20, 0)  # Gems Gained
        self.writeLong(21, 0)  # Looking For Team State
        self.writeLong(22, 1)
        self.writeLong(23, 0)  # Club Trophies Gained
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVInt(0) # count 0

        self.writeVInt(2) # count Brawl Pass Season
        for season in range(14, 16):

            self.writeVInt(season)
            self.writeVInt(34500)
            self.writeBoolean(True)
            self.writeVInt(0)


            self.writeByte(2) # Premium rewards claimed level
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)


            self.writeByte(1) # free rewards claimed level
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount) # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)
        self.writeVInt(0) # vanity item

        self.writeBoolean(False) # Power League Array
        self.writeInt(164) # Logic Daily Data end
        self.writeVInt(19) # Logic Conf Data begin

        self.writeVInt(32) # event slot id
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18)
        self.writeVInt(19)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)

        self.writeVInt(1) # event data count
        self.writeVInt(-1)
        self.writeVInt(32)
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(0)
        self.writeDataReference(15, 122) # map id
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # map maker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array start
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # chronos text entry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)

        self.writeVInt(0) #upcoming event count

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeVInt(0) #locked for chronos

        self.writeVInt(24)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000057)  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(29, 20)  # Skin Group Active For Campaign
        self.writeLong(48, 41381)
        self.writeLong(50, 0)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 0)  # Double Token Event
        self.writeLong(31, 1)  # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)
        self.writeLong(87, 1)

        self.writeVInt(0) #  Timed int entry count

        self.writeVInt(0) # custom event

        self.writeVInt(2) # new arrayvInt
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(2) # new arrayvInt
        self.writeVInt(1)
        self.writeVInt(-64)
        self.writeVInt(2) # new arrayvInt
        self.writeVInt(1)
        self.writeVInt(4)

        self.writeVInt(0) #new count v46

        self.writeVInt(0) #new count v46

        self.writeLong(0, 1) # Player ID

        self.writeVInt(0) # Notification factory

        self.writeVInt(-64)
        self.writeBoolean(False)
        self.writeVInt(0) # Gatcha drop
        self.writeVInt(0) # End of LogicClientHome

        self.writeVInt(0)
        self.writeBoolean(False)

        self.writeVInt(0) # new function v46
        self.writeBoolean(False) #something weird, contains multiples if check


        # self.writeVInt(0) #end of LogicClientHome

        #Logic Client Avatar begin
        self.writeVLong(0, 1)
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString('risporce')
        self.writeBoolean(False)
        self.writeString()

        self.writeVInt(17) # Commodity Count

        #self.writeVInt(0)

        self.writeVInt(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVInt(-1)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(-1)
        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)
        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)
        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0) # Array

        self.writeVInt(ownedBrawlersCount)
        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)
        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0) # hero star power and gadget

        self.writeVInt(ownedBrawlersCount)
        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array

        self.writeVInt(player.Gems) # Diamonds
        self.writeVInt(player.Gems) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(0) # Battle Count
        self.writeVInt(0) # WinCount
        self.writeVInt(0) # LoseCount
        self.writeVInt(0) # WinLooseStreak
        self.writeVInt(0) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion