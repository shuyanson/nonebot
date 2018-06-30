PRIVATE_FRIEND = 0x0001
PRIVATE_GROUP = 0x0002
PRIVATE_DISCUSS = 0x0004
PRIVATE_OTHER = 0x0008
PRIVATE = 0x000F
DISCUSS = 0x00F0
GROUP_MEMBER = 0x0100
GROUP_ADMIN = 0x0200
GROUP_OWNER = 0x0400
GROUP = 0x0F00
SUPERUSER = 0xF000
EVERYBODY = 0xFFFF

IS_NOBODY = 0x0000
IS_PRIVATE_FRIEND = PRIVATE_FRIEND
IS_PRIVATE_GROUP = PRIVATE_GROUP
IS_PRIVATE_DISCUSS = PRIVATE_DISCUSS
IS_PRIVATE_OTHER = PRIVATE_OTHER
IS_PRIVATE = PRIVATE
IS_DISCUSS = DISCUSS
IS_GROUP_MEMBER = GROUP_MEMBER
IS_GROUP_ADMIN = GROUP_MEMBER | GROUP_ADMIN
IS_GROUP_OWNER = GROUP_ADMIN | GROUP_OWNER
IS_GROUP = GROUP
IS_SUPERUSER = 0xFFFF