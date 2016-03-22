USE [FXTracker];

/****** Object:  Table [dbo].[TestTable]    Script Date: 2016-03-21 8:32:53 PM ******/
--DROP TABLE [dbo].[Tracker];

/****** Object:  Table [dbo].[TestTable]    Script Date: 2016-03-21 8:32:53 PM ******/
SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
SET ANSI_PADDING ON;

CREATE TABLE [dbo].[Tracker](
	[TrackerId] [int] IDENTITY(1,1) NOT NULL,
	[CreatedOn] [datetime] NULL DEFAULT (getdate()),
	[Userid] [nvarchar] (32) NULL,
	[Description] [nvarchar] (64) NULL
PRIMARY KEY CLUSTERED 
(
	[TrackerId] ASC
)	WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
)	ON [PRIMARY];
SET ANSI_PADDING OFF;