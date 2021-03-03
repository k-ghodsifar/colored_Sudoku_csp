class CSP_Node:
    def __init__(self,table_c,table_n,domain_n,domain_c,extra):
        self.table_c = table_c
        self.table_n = table_n
        self.domain_n = domain_n
        self.domain_c = domain_c
        self.degree_n = [0,0,0]
        self.degree_c = [0,0,0]
        self.child_n = []
        self.child_c = []

    def fourth_limit(self):
        # 4th limitation -------------------------------------------------------
        for i in range(n):
            for j in range(n):

                # numbers -----------------
                if self.table_n[i][j] != '*' and self.table_c[i][j] == '#':
                    if i-1 >= 0 :
                        if self.table_n[i-1][j] != '*' and self.table_c[i-1][j] != '#':
                            tmp_n3 = colors.index(self.table_c[i-1][j])
                            if self.table_n[i][j] > self.table_n[i-1][j]:
                                if tmp_n3 == m-1:
                                    return False

                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[:tmp_n3+1]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False

                            else:
                                if tmp_n3 == 0:
                                    return False

                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[tmp_n3:]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False


                if self.table_n[i][j] != '*' and self.table_c[i][j] == '#':
                    if i+1 < n :
                        if self.table_n[i+1][j] != '*' and self.table_c[i+1][j] != '#':
                            tmp_n3 = colors.index(self.table_c[i+1][j])
                            if self.table_n[i][j] > self.table_n[i+1][j]:
                                if tmp_n3 == m-1:
                                    return False

                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[:tmp_n3+1]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False

                            else:
                                if tmp_n3 == 0:
                                    return False

                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[tmp_n3:]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False

                if self.table_n[i][j] != '*' and self.table_c[i][j] == '#':
                    if j-1 >=  0 :
                        if self.table_n[i][j-1] != '*' and self.table_c[i][j-1] != '#':
                            tmp_n3 = colors.index(self.table_c[i][j-1])
                            if self.table_n[i][j] > self.table_n[i][j-1]:
                                if tmp_n3 == m-1:
                                    return False
                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[:tmp_n3+1]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False
                            else:
                                if tmp_n3 == 0:
                                    return False
                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[tmp_n3:]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False

                if self.table_n[i][j] != '*' and self.table_c[i][j] == '#':
                    if j+1 < n :
                        if self.table_n[i][j+1] != '*' and self.table_c[i][j+1] != '#':
                            tmp_n3 = colors.index(self.table_c[i][j+1])
                            if self.table_n[i][j] > self.table_n[i][j+1]:
                                if tmp_n3 == m-1:
                                    return False
                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[:tmp_n3+1]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False
                            else:
                                if tmp_n3 == 0:
                                    return False
                                else:
                                    for c in self.domain_c[i][j]:
                                        if c in colors[tmp_n3:]:
                                            self.domain_c[i][j].pop(self.domain_c[i][j].index(c))
                                    if len(self.domain_c[i][j]) == 0:
                                        return False

            # colors ----------------------
            if self.table_c[i][j] != '#' and self.table_n[i][j] == '*':
                if i-1 >= 0 :
                    if self.table_c[i-1][j] != '#' and self.table_n[i-1][j] != '*':
                        a = colors.index(self.table_c[i][j])
                        b = colors.index(self.table_c[i-1][j])
                        if a > b:
                            if b == m-1:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu <= self.table_n[i-1][j]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False
                        else:
                            if b == 0:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu >= self.table_n[i-1][j]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False

                if i+1 < n :
                    if self.table_c[i+1][j] != '#' and self.table_n[i+1][j] != '*':
                        a = colors.index(self.table_c[i][j])
                        b = colors.index(self.table_c[i+1][j])
                        if a > b:
                            if b == m-1:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu <= self.table_n[i+1][j]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False
                        else:
                            if b == 0:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu >= self.table_n[i+1][j]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False

                if j-1 >= 0 :
                    if self.table_c[i][j-1] != '#' and self.table_n[i][j-1] != '*':
                        a = colors.index(self.table_c[i][j])
                        b = colors.index(self.table_c[i][j-1])
                        if a > b:
                            if b == m-1:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu <= self.table_n[i][j-1]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False
                        else:
                            if b == 0:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu >= self.table_n[i][j-1]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False

                if j+1 < n :
                    if self.table_c[i][j-1] != '#' and self.table_n[i][j+1] != '*':
                        a = colors.index(self.table_c[i][j])
                        b = colors.index(self.table_c[i][j+1])
                        if a > b:
                            if b == m-1:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu <= self.table_n[i][j+1]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False
                        else:
                            if b == 0:
                                return False
                            else:
                                for nu in self.domain_n[i][j]:
                                    if nu >= self.table_n[i][j+1]:
                                        self.domain_n[i][j].pop(self.domain_n[i][j].index(nu))
                                if len(self.domain_n[i][j]) == 0:
                                    return False

        return True
        # ----------------------------------------------------------------------

    def MRV(self):
        mrv_tmp_c = [[m,0,0]]
        mrv_tmp_n = [[n,0,0]]
        # for colors
        for i in range(n):
            for j in range(n):
                if self.domain_c[i][j][0] != 'assigned' and len(self.domain_c[i][j]) < mrv_tmp_c[0][0]:
                    mrv_tmp_c.clear()
                    mrv_tmp_c.append([len(self.domain_c[i][j]),i,j])
                elif self.domain_c[i][j][0] != 'assigned' and len(self.domain_c[i][j]) == mrv_tmp_c[0][0]:
                    mrv_tmp_c.append([len(self.domain_c[i][j]),i,j])

        # for numbers
        for i in range(n):
            for j in range(n):
                if self.domain_n[i][j][0] != 'assigned' and len(self.domain_n[i][j]) < mrv_tmp_n[0][0]:
                    mrv_tmp_n.clear()
                    mrv_tmp_n.append([len(self.domain_n[i][j]),i,j])
                elif self.domain_n[i][j][0] != 'assigned' and len(self.domain_n[i][j]) == mrv_tmp_n[0][0]:
                    mrv_tmp_n.append([len(self.domain_n[i][j]),i,j])
        return( [mrv_tmp_c, mrv_tmp_n] )



    def Degree(self,i,j):
        tmpc2sum = []
        test1 = []
        if self.domain_c[i][j][0] != 'assigned':
            for k in range(n):
                if self.domain_c[i][k][0] != 'assigned':
                    tmpc2sum.append(1)
            for k in range(n):
                if self.domain_c[k][j][0] != 'assigned':
                    tmpc2sum.append(1)
        test1.append(len(tmpc2sum.copy()))
        tmpc2sum.clear()
        '''
        if self.domain_c[i][j][0] != 'assigned':
            if i-1 >= 0 :
                if self.domain_c[i-1][j][0] != 'assigned':
                    tmpc2sum.append(1)
            if i+1 < n :
                if self.domain_c[i+1][j][0] != 'assigned':
                    tmpc2sum.append(1)
            if j-1 >= 0:
                if self.domain_c[i][j-1][0] != 'assigned':
                    tmpc2sum.append(1)
            if j+1 < n:
                if self.domain_c[i][j+1][0] != 'assigned':
                    tmpc2sum.append(1)
            if len(tmpc2sum) > self.degree_c[0] :
                test1.append(len(tmpc2sum))
            tmpc2sum.clear()
        '''
        if self.domain_n[i][j][0] != 'assigned':
            for k in range(n):
                if self.domain_n[i][k][0] != 'assigned':
                    tmpc2sum.append(1)
            for k in range(n):
                if self.domain_n[k][j][0] != 'assigned':
                    tmpc2sum.append(1)
        test1.append(len(tmpc2sum.copy()))
        tmpc2sum.clear()
        '''
        if self.domain_n[i][j][0] != 'assigned':
            if i-1 >= 0 :
                if self.domain_n[i-1][j][0] != 'assigned':
                    tmpc2sum.append(1)
            if i+1 < n :
                if self.domain_n[i+1][j][0] != 'assigned':
                    tmpc2sum.append(1)
            if j-1 >= 0:
                if self.domain_n[i][j-1][0] != 'assigned':
                    tmpc2sum.append(1)
            if j+1 < n:
                if self.domain_n[i][j+1][0] != 'assigned':
                    tmpc2sum.append(1)
            if len(tmpc2sum) > self.degree_n[0] :
                test1.append(len(tmpc2sum))
            tmpc2sum.clear()
        '''
        return(test1.copy())

    def Degree1(self):
        tmpc2sum = []
        for i in range(n):
            for j in range(n):
                if self.domain_c[i][j][0] != 'assigned':
                    if i-1 >= 0 :
                        if self.domain_c[i-1][j][0] != 'assigned':
                            tmpc2sum.append(1)
                    if i+1 < n :
                        if self.domain_c[i+1][j][0] != 'assigned':
                            tmpc2sum.append(1)
                    if j-1 >= 0:
                        if self.domain_c[i][j-1][0] != 'assigned':
                            tmpc2sum.append(1)
                    if j+1 < n:
                        if self.domain_c[i][j+1][0] != 'assigned':
                            tmpc2sum.append(1)
                    if len(tmpc2sum) > self.degree_c[0] :
                        self.degree_c[0] = len(tmpc2sum)
                        self.degree_c[1] = i
                        self.degree_c[2] = j
                    tmpc2sum.clear()

        for i in range(n):
            for j in range(n):
                if self.domain_n[i][j][0] != 'assigned':
                    if i-1 >= 0 :
                        if self.domain_n[i-1][j][0] != 'assigned':
                            tmpc2sum.append(1)
                    if i+1 < n :
                        if self.domain_n[i+1][j][0] != 'assigned':
                            tmpc2sum.append(1)
                    if j-1 >= 0:
                        if self.domain_n[i][j-1][0] != 'assigned':
                            tmpc2sum.append(1)
                    if j+1 < n:
                        if self.domain_n[i][j+1][0] != 'assigned':
                            tmpc2sum.append(1)
                    if len(tmpc2sum) > self.degree_n[0] :
                        self.degree_n[0] = len(tmpc2sum)
                        self.degree_n[1] = i
                        self.degree_n[2] = j
                    tmpc2sum.clear()
        print(self.degree_c)
        print(self.degree_n)



    def is_goal(self):
        goal_test = []
        for i in range(n):
            for j in range(n):
                if self.table_c[i][j] == '#' or self.domain_n[i][j] == '*':
                    goal_test.append(0)
        if len(goal_test) == 0:
            print('--------goal found!-----------')
            self.Show()
            return True
        else:
            return False

    def is_goal_n(self):
        goal_test_n = []
        for i in range(n):
            for j in range(n):
                if self.table_n[i][j] == '*':
                    goal_test_n.append(0)
        if len(goal_test_n) == 0:
            print('--------goal numbers found!-----------')
            self.Show()
            return True
        else:
            return False

    def is_goal_c(self):
        goal_test_c = []
        for i in range(n):
            for j in range(n):
                if self.table_c[i][j] == '#':
                    goal_test_c.append(0)
        if len(goal_test_c) == 0:
            print('--------goal colors found!-----------')
            self.Show()
            return True
        else:
            return False

    def show_domain(self):
        '''
        print('---domain of colors---')
        for i in range(n):
            for j in range(n):
                print(self.domain_c[i][j],end=" ")
            print('\n')
        '''
        print('---domain of numbers---')
        for i in range(n):
            for j in range(n):
                print(self.domain_n[i][j],end=" ")
            print('\n')


    '''
    def backtrack(self): # solving by backtracking
    '''
    def FC(self,i,j):        # limit on domains by FC
        # FC for colors
        for k in range(n):
            if self.domain_c[i][k][0] != 'assigned':
                if self.table_c[i][j] in self.domain_c[i][k]:
                    self.domain_c[i][k].pop(self.domain_c[i][k].index(self.table_c[i][j]))
                    if len(self.domain_c[i][k]) == 0:
                        return False
        for k in range(n):
            if self.domain_c[k][j][0] != 'assigned':
                if self.table_c[i][j] in self.domain_c[k][j]:
                    self.domain_c[k][j].pop(self.domain_c[k][j].index(self.table_c[i][j]))
                    if len(self.domain_c[k][j]) == 0:
                        return False
        '''
        if i-1 >= 0 :
            if self.domain_c[i-1][j][0] != 'assigned':
                if self.table_c[i][j] in self.domain_c[i-1][j]:
                    self.domain_c[i-1][j].pop(self.domain_c[i-1][j].index(self.table_c[i][j]))
                    if len(self.domain_c[i-1][j]) == 0:
                        return False
        if i+1 < n :
            if self.domain_c[i+1][j][0] != 'assigned':
                if self.table_c[i][j] in self.domain_c[i+1][j]:
                    self.domain_c[i+1][j].pop(self.domain_c[i+1][j].index(self.table_c[i][j]))
                    if len(self.domain_c[i+1][j]) == 0:
                        return False
        if j-1 >= 0:
            if self.domain_c[i][j-1][0] != 'assigned':
                if self.table_c[i][j] in self.domain_c[i][j-1]:
                    self.domain_c[i][j-1].pop(self.domain_c[i][j-1].index(self.table_c[i][j]))
                    if len(self.domain_c[i][j-1]) == 0:
                        return False
        if j+1 < n:
            if self.domain_c[i][j+1][0] != 'assigned':
                if self.table_c[i][j] in self.domain_c[i][j+1]:
                    self.domain_c[i][j+1].pop(self.domain_c[i][j+1].index(self.table_c[i][j]))
                    if len(self.domain_c[i][j+1]) == 0:
                        return False
        '''

        # FC for numbers:
        for k in range(n):
            if self.domain_n[i][k][0] != 'assigned':
                if self.table_n[i][j] in self.domain_n[i][k]:
                    self.domain_n[i][k].pop(self.domain_n[i][k].index(self.table_n[i][j]))
                    if len(self.domain_n[i][k]) == 0:
                        return False
        for k in range(n):
            if self.domain_n[k][j][0] != 'assigned':
                if self.table_n[i][j] in self.domain_n[k][j]:
                    self.domain_n[k][j].pop(self.domain_n[k][j].index(self.table_n[i][j]))
                    if len(self.domain_n[k][j]) == 0:
                        return False
        '''
        if i-1 >= 0 :
            if self.domain_n[i-1][j][0] != 'assigned':
                if self.table_n[i][j] in self.domain_n[i-1][j]:
                    self.domain_n[i-1][j].pop(self.domain_n[i-1][j].index(self.table_n[i][j]))
                    if len(self.domain_n[i-1][j]) == 0:
                        print('E1')
                        return False
        if i+1 < n :
            if self.domain_n[i+1][j][0] != 'assigned':
                if self.table_n[i][j] in self.domain_n[i+1][j]:
                    self.domain_n[i+1][j].pop(self.domain_n[i+1][j].index(self.table_n[i][j]))
                    if len(self.domain_n[i+1][j]) == 0:
                        print('E2')
                        return False
        if j-1 >= 0:
            if self.domain_n[i][j-1][0] != 'assigned':
                if self.table_n[i][j] in self.domain_n[i][j-1]:
                    self.domain_n[i][j-1].pop(self.domain_n[i][j-1].index(self.table_n[i][j]))
                    if len(self.domain_n[i][j-1]) == 0:
                        print('E3')
                        return False
        if j+1 < n:
            if self.domain_n[i][j+1][0] != 'assigned':
                if self.table_n[i][j] in self.domain_n[i][j+1]:
                    self.domain_n[i][j+1].pop(self.domain_n[i][j+1].index(self.table_n[i][j]))
                    if len(self.domain_n[i][j+1]) == 0:
                        print('E4')
                        return False
        '''
        return True

    def Show(self):
        for i in range(n):
            for j in range(n):
                print(self.table_n[i][j],self.table_c[i][j],sep='',end=" ")
            print('\n')
    def __eq__(self, other):
        for i in rang(n):
            for j in range(n):
                if self.table_c[i][j] != other.table_c[i][j] or self.table_n[i][j] != other.table_n:
                    return False
        return True

    def Backtrack_c(self):
        print('-------------------------------------------')
        self.Show()
        self.show_domain()
        if self.is_goal_c() == False:
            mrv = self.MRV()
            print(mrv)
            test10 = []
            local_history = []
            for i in range(len(mrv[0])):
                test10.append([self.Degree(mrv[0][i][1],mrv[0][i][2]),i])
            test10.sort(key = lambda x: x[0],reverse = True)
            for t in test10:
                local_history.append([mrv[0][t[1]][1],mrv[0][t[1]][2]])
                for k in range(mrv[0][t[1]][0]):
                    cp_table_c = []
                    cp_domain_c = []
                    for l in range(n):
                        cp_domain_c.append([])
                    for l in range(n):
                        cp_table_c.append(self.table_c[l].copy())
                        for o in range(n):
                            cp_domain_c[l].append(self.domain_c[l][o].copy())
                    cp_table_c[mrv[0][t[1]][1]][mrv[0][t[1]][2]] = self.domain_c[mrv[0][t[1]][1]][mrv[0][t[1]][2]][k]
                    cp_domain_c[mrv[0][t[1]][1]][mrv[0][t[1]][2]].clear()
                    cp_domain_c[mrv[0][t[1]][1]][mrv[0][t[1]][2]].append('assigned')
                    ch = CSP_Node(cp_table_c.copy(),self.table_n.copy(),self.domain_n.copy(),cp_domain_c.copy(),[])
                    ch.Show()
                    ch.show_domain()
                    if (ch.FC(mrv[0][t[1]][1],mrv[0][t[1]][2])):
                        if( ch.fourth_limit() ):
                            self.child_c.append(ch)
                        else:
                            print('wrong FL1',mrv[0][t[1]][1],mrv[0][t[1]][2])
                    else:
                        print('wrong FC1',mrv[0][t[1]][1],mrv[0][t[1]][2])
            for i in range(n):
                for j in range(n):
                    if [i,j] not in local_history:
                        if self.table_c[i][j] == '#':
                            for k in range(len(self.domain_c[i][j])):
                                cp_table_c = []
                                cp_domain_c = []
                                for l in range(n):
                                    cp_domain_c.append([])
                                for l in range(n):
                                    cp_table_c.append(self.table_c[l].copy())
                                    for o in range(n):
                                        cp_domain_c[l].append(self.domain_c[l][o].copy())
                                cp_table_c[i][j] = self.domain_c[i][j][k]
                                cp_domain_c[i][j].clear()
                                cp_domain_c[i][j].append('assigned')
                                ch = CSP_Node(cp_table_c.copy(),self.table_n.copy(),self.domain_n.copy(),cp_domain_c.copy(),[])
                                if (ch.FC(i,j)):
                                    if( ch.fourth_limit() ):
                                        self.child_c.append(ch)
                                    else:
                                        print('wrong FL2',i,j)
                                else:
                                    print('wrong FC2',i,j)
            if len(self.child_c) > 0:
                first_node = self.child_c[0]
                self.child_c.pop(0)
                first_node.Backtrack_c()
            else:
                print('failture!')

    def Backtrack_n(self):
        print('-------------------------------------------')
        self.Show()
        self.show_domain()
        if self.is_goal_n() == True:
            print('```')
            #self.Backtrack_c()
        else:
            mrv = self.MRV()
            test10 = []
            local_history = []
            for i in range(len(mrv[1])):
                test10.append([self.Degree(mrv[1][i][1],mrv[1][i][2]),mrv[1][i][1],mrv[1][i][2]])
            test10.sort(key = lambda x: x[0],reverse = True)
            cp_table_n = []
            cp_domain_n = []
            for t in test10:
                local_history.append([t[1],t[2]])
                for k in range(len(self.domain_n[t[1]][t[2]])):
                    cp_table_n.clear()
                    cp_domain_n.clear()
                    for l in range(n):
                        cp_domain_n.append([])
                    for l in range(n):
                        cp_table_n.append(self.table_n[l].copy())
                        for o in range(n):
                            cp_domain_n[l].append(self.domain_n[l][o].copy())
                    cp_table_n[t[1]][t[2]] = self.domain_n[t[1]][t[2]][k]
                    #cp_table_n[mrv[1][t[1]][1]][mrv[1][t[1]][2]] = self.domain_n[mrv[1][t[1]][1]][mrv[1][t[1]][2]][k]
                    cp_domain_n[t[1]][t[2]].clear()
                    #cp_domain_n[mrv[1][t[1]][1]][mrv[1][t[1]][2]].clear()
                    cp_domain_n[t[1]][t[2]].append('assigned')
                    #cp_domain_n[mrv[1][t[1]][1]][mrv[1][t[1]][2]].append('assigned')
                    ch = CSP_Node(self.table_c.copy(),cp_table_n.copy(),cp_domain_n.copy(),self.domain_c.copy(),[])
                    if( ch.FC(t[1],t[2]) ):
                    #if (ch.FC(mrv[1][t[1]][1],mrv[1][t[1]][2])):
                        if( ch.fourth_limit() ):
                            print('HHHHHHHHHH',t[1],t[2],self.domain_n[t[1]][t[2]][k])
                            self.child_n.append(ch)
                        else:
                            print('wrong FL1',t[1],t[2])
                            #print('wrong FL1',mrv[1][t[1]][1],mrv[1][t[1]][2])
                    else:
                        print('wrong FC1',mrv[1][t[1]][1],mrv[1][t[1]][2])
            for i in range(n):
                for j in range(n):
                    if [i,j] not in local_history:
                        if self.table_n[i][j] == '*':
                            for k in range(len(self.domain_n[i][j])):
                                cp_table_n = []
                                cp_domain_n = []
                                for l in range(n):
                                    cp_domain_n.append([])
                                for l in range(n):
                                    cp_table_n.append(self.table_n[l].copy())
                                    for o in range(n):
                                        cp_domain_n[l].append(self.domain_n[l][o].copy())
                                cp_table_n[i][j] = self.domain_n[i][j][k]
                                cp_domain_n[i][j].clear()
                                cp_domain_n[i][j].append('assigned')
                                ch = CSP_Node(self.table_c.copy(),cp_table_n.copy(),cp_domain_n.copy(),self.domain_c.copy(),[])
                                if (ch.FC(i,j)):
                                    if( ch.fourth_limit() ):
                                        self.child_n.append(ch)
                                    else:
                                        print('wrong FL2',i,j)
                                else:
                                    print('wrong FC2',i,j)
            if len(self.child_n) > 0:
                first_node = self.child_n[0]
                self.child_n.pop(0)
                first_node.Backtrack_n()
            




# initializing first state (start node)
first_line = input().split()
col = input().split()
m = eval(first_line[0]) # number of colors
n = eval(first_line[1]) # table size
colors = []
for i in range(m):
    colors.append(col[m-1-i])
table_n = []
table_c = []
for i in range(n):
    table_n.append([])
    table_c.append([])
tmp = ''
for i in range(n):
    tmp = input().split().copy()
    for j in range(n):
        if tmp[j][0] != '*':
            table_n[i].append(eval(tmp[j][0:-1]))
        else:
            table_n[i].append(tmp[j][0])
        table_c[i].append(tmp[j][-1])
# calculate domains ------------------------------------------------------------
domain_c = []
domain_n = []
for i in range(n):
    domain_n.append([])
    domain_c.append([])
    for j in range(n):
        domain_n[i].append([])
        domain_c[i].append([])
tmpc1 = []
tmpn1 = []
for i in range(n):
    for j in range(n):
        if table_c[i][j] != '#':
            domain_c[i][j].append('assigned')
        else:
            for c in colors:
                if c not in table_c[i]:
                    for k in range(n):
                        if c != table_c[k][j]:
                            tmpc1.append(0)
                if len(tmpc1) == n:
                    domain_c[i][j].append(c)
                tmpc1.clear()
        if table_n[i][j] != '*':
            domain_n[i][j].append('assigned')
        else:
            for c in range(n):
                c = c+1
                if c not in table_n[i]:
                    for k in range(n):
                        if c != table_n[k][j]:
                            tmpn1.append(0)
                if len(tmpn1) == n:
                    domain_n[i][j].append(c)
                tmpn1.clear()
# ------------------------------------------------------------------------------
start = CSP_Node(table_c,table_n,domain_n,domain_c,[])
start.fourth_limit()
start.Backtrack_n()
