(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[229],{7938:function(l,i,s){(window.__NEXT_P=window.__NEXT_P||[]).push(["/match-news/[name]",function(){return s(9898)}])},9898:function(l,i,s){"use strict";s.r(i),s.d(i,{default:function(){return _}});var e=s(5893),n=s(7294),d=s(9008),o=s.n(d),c=s(7931),r=s(4811),a=s(1230),v=s(5746),t=s(6115),h=s(381),u=s.n(h),m=s(9473),x=s(1163),j=s(7618),p=s(1413),Z={icon:{tag:"svg",attrs:{viewBox:"64 64 896 896",focusable:"false"},children:[{tag:"path",attrs:{d:"M752 664c-28.5 0-54.8 10-75.4 26.7L469.4 540.8a160.68 160.68 0 000-57.6l207.2-149.9C697.2 350 723.5 360 752 360c66.2 0 120-53.8 120-120s-53.8-120-120-120-120 53.8-120 120c0 11.6 1.6 22.7 4.7 33.3L439.9 415.8C410.7 377.1 364.3 352 312 352c-88.4 0-160 71.6-160 160s71.6 160 160 160c52.3 0 98.7-25.1 127.9-63.8l196.8 142.5c-3.1 10.6-4.7 21.8-4.7 33.3 0 66.2 53.8 120 120 120s120-53.8 120-120-53.8-120-120-120zm0-476c28.7 0 52 23.3 52 52s-23.3 52-52 52-52-23.3-52-52 23.3-52 52-52zM312 600c-48.5 0-88-39.5-88-88s39.5-88 88-88 88 39.5 88 88-39.5 88-88 88zm440 236c-28.7 0-52-23.3-52-52s23.3-52 52-52 52 23.3 52 52-23.3 52-52 52z"}}]},name:"share-alt",theme:"outlined"},f=s(2135),N=function(l,i){return n.createElement(f.Z,(0,p.Z)((0,p.Z)({},l),{},{ref:i,icon:Z}))};N.displayName="ShareAltOutlined";var b=n.forwardRef(N),y=s(7062),_=function(l){var i,s,d,h,p,Z,f,N,_,L,T,S,w,D,g,E,A,O,k,C,R,H,M,z,Y,G,K,P,I,X,q,B,F,J,V,Q,U,W,$,ll,li,ls,le,ln,ld,lo,lc,lr,la,lv,lt,lh,lu,lm,lx,lj,lp,lZ,lf,lN,lb,ly,l_,lL,lT,lS,lw,lD,lg,lE,lA,lO;let lk=(0,x.useRouter)(),{name:lC}=lk.query,lR=(0,m.I0)(),lH=(0,m.v9)(l=>l.auth.homeSettings),lM=(0,m.v9)(l=>l.score.highlights);t.Z.token;let[lz,lY]=(0,n.useState)(1),{TabPane:lG}=r.Z,lK=(null==lM?void 0:lM.commentary)?lM.commentary:{},lP=(null==lM?void 0:lM.scorecard)?lM.scorecard:{};null==lM||lM.highlights;let lI=(null==lM?void 0:lM.matches)?{...lM.matches,venue:(null==lM?void 0:null===(i=lM.matches)||void 0===i?void 0:i.venue)?JSON.parse(lM.matches.venue):{}}:{};(null==lM?void 0:lM.facts)&&lM.facts;let lX=(null===(s=null==lM?void 0:null===(d=lM.live_details)||void 0===d?void 0:d.scorecard[0])||void 0===s?void 0:s.still_to_bat)?null===(h=null==lM?void 0:null===(p=lM.live_details)||void 0===p?void 0:p.scorecard[0])||void 0===h?void 0:h.still_to_bat:[];return(0,n.useEffect)(()=>{window.scrollTo(0,0),lR((0,j._Y)(lC)),y.Z.subscribe(lC)},[lC]),(0,e.jsxs)(c.Z,{children:[(0,e.jsxs)(o(),{children:[(0,e.jsx)("title",{children:null==lH?void 0:lH.meta_title}),(0,e.jsx)("meta",{name:"description",content:null==lH?void 0:lH.meta_description})]}),(0,e.jsx)("div",{className:"container",children:(0,e.jsx)("div",{className:"score-board",children:(0,e.jsxs)("div",{className:"wickets",children:[(0,e.jsxs)("h5",{children:[null==lK?void 0:null===(Z=lK.matchHeader)||void 0===Z?void 0:null===(f=Z.team1)||void 0===f?void 0:f.name," vs  ",null==lK?void 0:null===(N=lK.matchHeader)||void 0===N?void 0:null===(_=N.team2)||void 0===_?void 0:_.name,", ",null==lK?void 0:null===(L=lK.matchHeader)||void 0===L?void 0:L.matchDescription]}),(0,e.jsxs)("span",{children:["Series: ",(0,e.jsx)("a",{href:"#",children:null==lK?void 0:null===(T=lK.matchHeader)||void 0===T?void 0:T.seriesName})]}),(0,e.jsxs)("span",{children:["Venue:  ",(0,e.jsxs)("a",{href:"#",children:[null==lI?void 0:null===(S=lI.venue)||void 0===S?void 0:S.ground,", ",null==lI?void 0:null===(w=lI.venue)||void 0===w?void 0:w.city]})]}),(0,e.jsxs)("span",{children:["Date & Time: ",(0,e.jsx)("a",{href:"#",children:u().utc(null==lI?void 0:lI.startdt).format("Do MMM YYYY hh:mm A")})]}),(0,e.jsxs)(r.Z,{defaultActiveKey:"1",children:[(0,e.jsx)(lG,{tab:"Commentary",children:(0,e.jsx)(r.Z,{defaultActiveKey:"1",children:(0,e.jsxs)(lG,{tab:null==lM?void 0:null===(D=lM.live_details)||void 0===D?void 0:null===(g=D.scorecard)||void 0===g?void 0:null===(E=g[0])||void 0===E?void 0:E.title,children:[(0,e.jsxs)("h5",{className:"tem-scro",children:[null==lK?void 0:null===(A=lK.miniscore)||void 0===A?void 0:null===(O=A.matchScoreDetails)||void 0===O?void 0:null===(k=O.inningsScoreList)||void 0===k?void 0:null===(C=k[0])||void 0===C?void 0:C.batTeamName," /",null==lK?void 0:null===(R=lK.miniscore)||void 0===R?void 0:null===(H=R.matchScoreDetails)||void 0===H?void 0:null===(M=H.inningsScoreList)||void 0===M?void 0:null===(z=M[1])||void 0===z?void 0:z.wickets," (50)"]}),(0,e.jsxs)("h5",{children:[null==lK?void 0:null===(Y=lK.miniscore)||void 0===Y?void 0:null===(G=Y.matchScoreDetails)||void 0===G?void 0:null===(K=G.inningsScoreList)||void 0===K?void 0:null===(P=K[1])||void 0===P?void 0:P.batTeamName," ",null==lK?void 0:null===(I=lK.miniscore)||void 0===I?void 0:null===(X=I.matchScoreDetails)||void 0===X?void 0:null===(q=X.inningsScoreList)||void 0===q?void 0:null===(B=q[0])||void 0===B?void 0:B.score," ",null==lK?void 0:null===(F=lK.miniscore)||void 0===F?void 0:null===(J=F.matchScoreDetails)||void 0===J?void 0:null===(V=J.inningsScoreList)||void 0===V?void 0:null===(Q=V[0])||void 0===Q?void 0:Q.overs]}),(0,e.jsx)("p",{className:"australia-tem",children:null==lK?void 0:null===(U=lK.miniscore)||void 0===U?void 0:U.status}),(0,e.jsx)("p",{children:"PLAYER OF THE MATCH"}),(0,e.jsx)("span",{children:(0,e.jsxs)("a",{href:"#",color:"black",children:[null==lK?void 0:null===(W=lK.matchHeader)||void 0===W?void 0:null===($=W.playersOfTheMatch)||void 0===$?void 0:null===(ll=$[0])||void 0===ll?void 0:ll.fullName," "]})}),(0,e.jsx)("div",{className:"score"}),(0,e.jsx)("p",{className:"closer",children:(0,e.jsx)("a",{href:"#",children:"Stay closer to Cricket, always! Get the cricbuzz app for your mobile"})}),(0,e.jsx)("div",{className:"score"}),(0,e.jsx)("div",{className:"comprehensive",children:(null==lK?void 0:lK.commentaryList)?null==lK?void 0:lK.commentaryList.map((l,i)=>(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==l?void 0:l.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==l?void 0:l.commText})]},i)):null}),(0,e.jsxs)("div",{className:"cost",children:[(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:20,children:(0,e.jsx)("p",{children:"The cost"})}),(0,e.jsx)(v.Z,{span:4,children:(0,e.jsx)(b,{className:"shree"})})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:"38.1"})}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsx)("p",{children:"Runs Scored: 0"}),(0,e.jsx)("h5",{children:"0 0 0 0 0 0"})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsx)("p",{children:"Score after 37 overs"}),(0,e.jsx)("h5",{children:"ENG 203-9"})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsxs)("p",{children:["Adil Rashid ",(0,e.jsx)("span",{children:"3(4)"})]}),(0,e.jsxs)("h5",{children:["Liam Dawson ",(0,e.jsx)("span",{children:"3(4)"})]})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsx)("p",{children:"Runs Scored: 0"}),(0,e.jsx)("h5",{children:"0 0 0 0 0 0"})]})]})]}),(0,e.jsxs)("div",{className:"comprehensive",children:[(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(li=lK.commentaryList)||void 0===li?void 0:null===(ls=li[12])||void 0===ls?void 0:ls.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(le=lK.commentaryList)||void 0===le?void 0:null===(ln=le[12])||void 0===ln?void 0:ln.commText})]}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(ld=lK.commentaryList)||void 0===ld?void 0:null===(lo=ld[13])||void 0===lo?void 0:lo.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(lc=lK.commentaryList)||void 0===lc?void 0:null===(lr=lc[13])||void 0===lr?void 0:lr.commText})]}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(la=lK.commentaryList)||void 0===la?void 0:null===(lv=la[14])||void 0===lv?void 0:lv.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(lt=lK.commentaryList)||void 0===lt?void 0:null===(lh=lt[14])||void 0===lh?void 0:lh.commText})]}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(lu=lK.commentaryList)||void 0===lu?void 0:null===(lm=lu[15])||void 0===lm?void 0:lm.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(lx=lK.commentaryList)||void 0===lx?void 0:null===(lj=lx[15])||void 0===lj?void 0:lj.commText})]}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(lp=lK.commentaryList)||void 0===lp?void 0:null===(lZ=lp[16])||void 0===lZ?void 0:lZ.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(lf=lK.commentaryList)||void 0===lf?void 0:null===(lN=lf[16])||void 0===lN?void 0:lN.commText})]}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(lb=lK.commentaryList)||void 0===lb?void 0:null===(ly=lb[17])||void 0===ly?void 0:ly.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(l_=lK.commentaryList)||void 0===l_?void 0:null===(lL=l_[17])||void 0===lL?void 0:lL.commText})]})]}),(0,e.jsxs)("div",{className:"cost",children:[(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:20,children:(0,e.jsx)("p",{children:"The cost"})}),(0,e.jsx)(v.Z,{span:4,children:(0,e.jsx)(b,{className:"shree"})})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:"38.1"})}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsx)("p",{children:"Runs Scored: 0"}),(0,e.jsx)("h5",{children:"0 0 0 0 0 0"})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsx)("p",{children:"Score after 37 overs"}),(0,e.jsx)("h5",{children:"ENG 203-9"})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsxs)("p",{children:["Adil Rashid ",(0,e.jsx)("span",{children:"3(4)"})]}),(0,e.jsxs)("h5",{children:["Liam Dawson ",(0,e.jsx)("span",{children:"3(4)"})]})]}),(0,e.jsx)("div",{className:"score"}),(0,e.jsxs)(v.Z,{span:4,offset:1,children:[(0,e.jsx)("p",{children:"Runs Scored: 0"}),(0,e.jsx)("h5",{children:"0 0 0 0 0 0"})]})]})]}),(0,e.jsxs)("div",{className:"comprehensive",children:[(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(lT=lK.commentaryList)||void 0===lT?void 0:null===(lS=lT[18])||void 0===lS?void 0:lS.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(lw=lK.commentaryList)||void 0===lw?void 0:null===(lD=lw[18])||void 0===lD?void 0:lD.commText})]}),(0,e.jsxs)(a.Z,{children:[(0,e.jsx)(v.Z,{span:2,children:(0,e.jsx)("h5",{children:null==lK?void 0:null===(lg=lK.commentaryList)||void 0===lg?void 0:null===(lE=lg[19])||void 0===lE?void 0:lE.overNumber})}),(0,e.jsx)(v.Z,{span:20,children:null==lK?void 0:null===(lA=lK.commentaryList)||void 0===lA?void 0:null===(lO=lA[19])||void 0===lO?void 0:lO.commText})]})]})]},"1")})},"1"),(0,e.jsx)(lG,{tab:"Scorecard",children:(0,e.jsx)(r.Z,{defaultActiveKey:"1",children:(0,e.jsx)(lG,{children:lP.scoreCard&&lP.scoreCard.map((l,i)=>{var s,n,d,o,c,r,a,v,t;return Object.values((null==l?void 0:null===(s=l.batTeamDetails)||void 0===s?void 0:s.batsmenData)?l.batTeamDetails.batsmenData:{}),Object.values((null==l?void 0:null===(n=l.bowlTeamDetails)||void 0===n?void 0:n.bowlersData)?l.bowlTeamDetails.bowlersData:{}),(0,e.jsxs)("div",{className:"scorecard-tab",children:[(0,e.jsxs)("h5",{children:[l.batTeamDetails.batTeamName," Innings",(0,e.jsx)("span",{children:"280-8 (50 Ov)"})]}),(0,e.jsxs)("div",{className:"total-scre",children:[(0,e.jsx)("h6",{children:"TOTAL"}),(0,e.jsx)("span",{children:null==lM?void 0:null===(d=lM.live_details)||void 0===d?void 0:null===(o=d.match_summary)||void 0===o?void 0:o.home_scores}),(0,e.jsx)("h6",{children:null==lM?void 0:null===(c=lM.live_details)||void 0===c?void 0:null===(r=c.match_summary)||void 0===r?void 0:r.away_scores})]}),(0,e.jsxs)("div",{children:[(0,e.jsx)("h6",{children:lX.map((l,i)=>(0,e.jsx)("a",{href:"#",children:l.player_name},i))}),(0,e.jsx)("p",{children:null==lM?void 0:null===(a=lM.live_details)||void 0===a?void 0:null===(v=a.scorecard)||void 0===v?void 0:null===(t=v[0])||void 0===t?void 0:t.fow})]})]},i)})})})},"2")]})]})})})]})}}},function(l){l.O(0,[571,885,743,695,634,931,774,888,179],function(){return l(l.s=7938)}),_N_E=l.O()}]);