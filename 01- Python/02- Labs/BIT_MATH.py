
########### SET BIT ###########
def SET_BIT(REG,BIT_POSITION):
    REG |= (1<<BIT_POSITION) 
    return REG
########## CLEAR BIT ##########
def CLEAR_BIT(REG,BIT_POSITION):
    REG &= ~(1<<BIT_POSITION) 
    return REG
########## TOGGEL BIT #########
def TOGGLE_BIT(REG,BIT_POSITION):
    REG ^= (1<<BIT_POSITION) 
    return REG
########## GET BIT ###########
def GET_BIT(REG,BIT_POSITION):
    REG & (1<<BIT_POSITION) 
    return REG


