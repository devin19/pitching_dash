#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:09:38 2020

@author: devinclementi
"""

import streamlit as st
import numpy as np
import pandas as pd
from sklearn import cluster, datasets, mixture
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.style.use('fivethirtyeight')

# Title for Dashboard
phillies = 'phillies_logo.png'
st.image(phillies)
st.title('Evaluating Our Pitchers')

# Import Pitching Data
ibp_pitch = pd.read_csv('ibp_pitcher.csv')

# Give option for DataFrame
if st.checkbox('Show Data'):
    ibp_pitch
    
# Filter DataFrames by Before/After All-Star Break
after_break = pd.DataFrame(ibp_pitch.query('all_star=="after"'))
before_break = pd.DataFrame(ibp_pitch.query('all_star=="before"'))
    
# Filter DataFrames by Pitchers Before and After Break
pitcher1a = pd.DataFrame(after_break.query('pitcherid==1'))
pitcher1b = pd.DataFrame(before_break.query('pitcherid==1'))

pitcher2a = pd.DataFrame(after_break.query('pitcherid==2'))
pitcher2b = pd.DataFrame(before_break.query('pitcherid==2'))

pitcher3a = pd.DataFrame(after_break.query('pitcherid==3'))
pitcher3b = pd.DataFrame(before_break.query('pitcherid==3'))

# Filter DataFrame by Pitcher
pitcher1 = pd.DataFrame(ibp_pitch.query('pitcherid==1'))
pitcher2 = pd.DataFrame(ibp_pitch.query('pitcherid==2'))
pitcher3 = pd.DataFrame(ibp_pitch.query('pitcherid==3'))

# Filter by Balls and Strikes
balls = pd.DataFrame(ibp_pitch.query('pitch_result=="ball"'))
strikes = pd.DataFrame(ibp_pitch.query('pitch_result=="called_strike"'))

#

st.sidebar.title('Choose a Pitcher')

pitcher_option = st.sidebar.selectbox('Which pitcher would you like to evaluate?', ['Pitcher 1', 'Pitcher 2', 'Pitcher 3'])

# Pitcher 1
if pitcher_option == 'Pitcher 1':
    
    chart_options = st.selectbox('Which chart would you like to view?', ['Pitch Break Chart', 'Pitch Selection', 'Spin Rate', 'Velocity', 'Pitch Location', 'Catchers'])
    
    # Break Charts
    if chart_options == 'Pitch Break Chart':
        st.write('## Pitcher 1 Break Charts')
        
        if st.checkbox('P1 Before Break'):
            break_chart1b = pitcher1b.query('pitch_type=="FF"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), color='red', label='Fastball')
            pitcher1b.query('pitch_type=="CH"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1b, color='blue', label='Changeup')
            pitcher1b.query('pitch_type=="CT"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1b, color='purple', label='Cutter')
            pitcher1b.query('pitch_type=="SL"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1b, color='yellow', label='Slider')
            pitcher1b.query('pitch_type=="CB"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1b, color='green', label='Curveball')
            
            break_chart1b.set_ylabel('Vertical Movement')
            break_chart1b.set_xlabel('Horizontal Movement')
            break_chart1b.legend()
            
            st.pyplot()
            
        if st.checkbox('P1 After Break'):
            break_chart1a = pitcher1a.query('pitch_type=="FF"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), color='red', label='Fastball')
            pitcher1a.query('pitch_type=="CH"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1a, color='blue', label='Changeup')
            pitcher1a.query('pitch_type=="CT"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1a, color='purple', label='Cutter')
            pitcher1a.query('pitch_type=="SL"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1a, color='yellow', label='Slider')
            pitcher1a.query('pitch_type=="CB"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart1a, color='green', label='Curveball')
        
            break_chart1a.set_ylabel('Vertical Movement')
            break_chart1a.set_xlabel('Horizontal Movement')
            break_chart1a.legend()
            
            st.pyplot()
        
    # Pitch Selection Pie Charts
    if chart_options == 'Pitch Selection':
        st.write('## Pitcher 1 Pitch Selection')
        
        if st.checkbox('P1 Pitches Before Break'):
            p1b_pitch_counts = pitcher1b.pitch_type.value_counts()
            p1b_pitch_pie = p1b_pitch_counts.plot(kind='pie', colors=['red', 'blue', 'purple', 'yellow', 'green', 'orange'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p1b_pitch_counts
            
            st.pyplot()
        
        if st.checkbox('P1 Pitches After Break'):
            p1a_pitch_counts = pitcher1a.pitch_type.value_counts()
            p1a_pitch_pe = p1a_pitch_counts.plot(kind='pie', colors=['red', 'blue', 'purple', 'yellow', 'green'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p1a_pitch_counts
        
            st.pyplot()
    
    # Spin Rate Bar Charts
    if chart_options == 'Spin Rate':
        st.write('## Pitcher 1 Spin Rates')
               
        p1_spin_rates = pd.DataFrame(pitcher1b.groupby('pitch_type')['spin_rate'].mean())
        p1_spin_rates['after_break'] = pd.DataFrame(pitcher1a.groupby('pitch_type')['spin_rate'].mean())
        p1_spin_rates.rename(columns = {'spin_rate':'before_break'}, inplace = True)
        p1_spin_rates
        
        p1_spin_rates_bar = p1_spin_rates.plot(kind='bar')
        
        st.pyplot()
        
    # Average Velo Bar Charts
    if chart_options == 'Velocity':
        st.write('## Pitcher 1 Average Velocities')
               
        p1_velo = pd.DataFrame(pitcher1b.groupby('pitch_type')['release_velo'].mean())
        p1_velo['after_break'] = pd.DataFrame(pitcher1a.groupby('pitch_type')['release_velo'].mean())
        p1_velo.rename(columns = {'release_velo':'before_break'}, inplace = True)
        p1_velo
        
        p1_velo_bar = p1_velo.plot(kind='bar')
        
        st.pyplot()
        
    # Strike Chart
    if chart_options == 'Pitch Location':
        st.write('## Pitcher 1 Pitch Location')
        
        # Pitch Location by Handedness of Batter
        handedness = st.selectbox('Righties, Lefties, or both?', ['Righties', 'Lefties', 'Both'])
        
        if handedness == 'Both':
            
            if st.checkbox('P1 Location Before Break'):
                
                location_chart1b = pitcher1b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                pitcher1b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1b, color='blue', label='Changeup')
                pitcher1b.query('pitch_type=="CT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1b, color='purple', label='Cutter')
                pitcher1b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1b, color='yellow', label='Slider')
                pitcher1b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1b, color='green', label='Curveball')
                
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart1b.legend()
                
                location_chart1b.add_patch(rect)
                
                st.pyplot()
            
            if st.checkbox('P1 Location After Break'):
                
                location_chart1a = pitcher1a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                pitcher1a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1a, color='blue', label='Changeup')
                pitcher1a.query('pitch_type=="CT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1a, color='purple', label='Cutter')
                pitcher1a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1a, color='yellow', label='Slider')
                pitcher1a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1a, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart1a.legend()
                
                location_chart1a.add_patch(rect)
                
                st.pyplot()
        
        if handedness == 'Righties':
            st.write('## Pitcher 1 Pitch Location Against Righties')
            
            if st.checkbox('P1 Location Before Break (R)'):
                righties_p1b = pd.DataFrame(pitcher1b.query('bats=="R"'))
                
                righties_p1b_count = righties_p1b.pitch_type.value_counts()
                
                righties_p1b_count
                
                location_chart1rb = righties_p1b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                righties_p1b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1rb, color='blue', label='Changeup')
                righties_p1b.query('pitch_type=="CT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1rb, color='purple', label='Cutter')
                righties_p1b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1rb, color='yellow', label='Slider')
                righties_p1b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1rb, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart1rb.legend()
                
                location_chart1rb.add_patch(rect)
                
                st.pyplot()
                
                
                
            if st.checkbox('P1 Location After Break (R)'):
                righties_p1a = pd.DataFrame(pitcher1a.query('bats=="R"'))
                
                righties_p1a_count = righties_p1a.pitch_type.value_counts()
                
                righties_p1a_count
                
                location_chart1ra = righties_p1a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                righties_p1a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1ra, color='blue', label='Changeup')
                righties_p1a.query('pitch_type=="CT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1ra, color='purple', label='Cutter')
                righties_p1a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1ra, color='yellow', label='Slider')
                righties_p1a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1ra, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart1ra.legend()
                
                location_chart1ra.add_patch(rect)
                
                st.pyplot()
                
        
        if handedness == 'Lefties':   
            st.write('## Pitcher 1 Pitch Selection Against Lefties')
                     
            if st.checkbox('P1 Location Before Break (L)'):
                lefties_p1b = pd.DataFrame(pitcher1b.query('bats=="L"'))
                
                lefties_p1b_count = lefties_p1b.pitch_type.value_counts()
                
                lefties_p1b_count
                
                location_chart1lb = lefties_p1b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                lefties_p1b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1lb, color='blue', label='Changeup')
                lefties_p1b.query('pitch_type=="CT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1lb, color='purple', label='Cutter')
                lefties_p1b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1lb, color='yellow', label='Slider')
                lefties_p1b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1lb, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart1lb.legend()
                
                location_chart1lb.add_patch(rect)
                
                st.pyplot()
                
            if st.checkbox('P1 Location After Break (L)'):
                lefties_p1a = pd.DataFrame(pitcher1a.query('bats=="L"'))
                
                lefties_p1a_count = lefties_p1a.pitch_type.value_counts()
                
                lefties_p1a_count
                
                location_chart1la = lefties_p1a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                lefties_p1a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1la, color='blue', label='Changeup')
                lefties_p1a.query('pitch_type=="CT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1la, color='purple', label='Cutter')
                lefties_p1a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1la, color='yellow', label='Slider')
                lefties_p1a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart1la, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart1la.legend()
                
                location_chart1la.add_patch(rect)
                
                st.pyplot()
    
    # Catcher Pie Charts
    if chart_options == 'Catchers':
        st.write('## Pitcher 1 Catchers')
        
        if st.checkbox('P1 Catchers Before Break'):
            p1b_catchers = pitcher1b.catcherid.value_counts()
            p1b_catcher_pie = p1b_catchers.plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p1b_catchers
            
            st.pyplot()
        
        if st.checkbox('P1 Catchers After Break'):
            p1a_catchers = pitcher1a.catcherid.value_counts()
            p1a_catcher_pie = p1a_catchers.plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p1a_catchers
        
            st.pyplot()
            
        if st.checkbox('Catcher Strike Percentages'):
            p1_balls = pd.DataFrame(balls.query('pitcherid==1'))
            p1_strikes = pd.DataFrame(strikes.query('pitcherid==1'))
            p1_catchers = pd.DataFrame(p1_balls.groupby('catcherid')['pitch_result'].count())
            p1_catchers['strikes'] = pd.DataFrame(p1_strikes.groupby('catcherid')['pitch_result'].count())
            p1_catchers.rename(columns = {'pitch_result':'balls'}, inplace = True)
            p1_catchers
            
            p1_catcher_framing = p1_catchers.iloc[0].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            
            p1_catcher_framing = p1_catchers.iloc[1].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            
        
# Pitcher 2
if pitcher_option == 'Pitcher 2':
    
    chart_options = st.selectbox('Which chart would you like to view?', ['Pitch Break Chart', 'Pitch Selection', 'Spin Rate', 'Velocity', 'Pitch Location', 'Catchers'])
    
    # Break Charts
    if chart_options == 'Pitch Break Chart':
        st.write('## Pitcher 2 Break Charts')
        
        if st.checkbox('P2 Before Break'):
            break_chart2b = pitcher2b.query('pitch_type=="FF"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), color='red', label='Fastball')
            pitcher2b.query('pitch_type=="CH"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2b, color='blue', label='Changeup')
            pitcher2b.query('pitch_type=="FT"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2b, color='grey', label='Two-Seam Fastball')
            pitcher2b.query('pitch_type=="SL"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2b, color='yellow', label='Slider')
            pitcher2b.query('pitch_type=="CB"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2b, color='green', label='Curveball')
            
            break_chart2b.set_ylabel('Vertical Movement')
            break_chart2b.set_xlabel('Horizontal Movement')
            break_chart2b.legend()
            
            st.pyplot()
            
        if st.checkbox('P2 After Break'):
            break_chart2a = pitcher2a.query('pitch_type=="FF"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), color='red', label='Fastball')
            pitcher2a.query('pitch_type=="CH"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2a, color='blue', label='Changeup')
            pitcher2a.query('pitch_type=="FT"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2a, color='grey', label='Two-Seam Fastball')
            pitcher2a.query('pitch_type=="SL"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2a, color='yellow', label='Slider')
            pitcher2a.query('pitch_type=="CB"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart2a, color='green', label='Curveball')
            
            break_chart2a.set_ylabel('Vertical Movement')
            break_chart2a.set_xlabel('Horizontal Movement')
            break_chart2a.legend()
            
            st.pyplot()
        
    # Pitch Selection Pie Charts
    if chart_options == 'Pitch Selection':
        st.write('## Pitcher 2 Pitch Selection')
        if st.checkbox('P2 Pitches Before Break'):
            p2b_pitch_counts = pitcher2b.pitch_type.value_counts()
            p2b_pitch_pie = p2b_pitch_counts.plot(kind='pie', colors=['red', 'blue', 'purple', 'yellow', 'green'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p2b_pitch_counts
            
            st.pyplot()
        
        if st.checkbox('P2 Pitches After Break'):
            p2a_pitch_counts = pitcher2a.pitch_type.value_counts()
            p2a_pitch_pie = p2a_pitch_counts.plot(kind='pie', colors=['red', 'purple', 'blue', 'yellow', 'green'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p2a_pitch_counts
            
            st.pyplot()   
        
    # Spin Rate Bar Charts
    if chart_options == 'Spin Rate':
        st.write('## Pitcher 2 Spin Rates')
                
        p2_spin_rates = pd.DataFrame(pitcher2b.groupby('pitch_type')['spin_rate'].mean())
        p2_spin_rates['after_break'] = pd.DataFrame(pitcher2a.groupby('pitch_type')['spin_rate'].mean())
        p2_spin_rates.rename(columns = {'spin_rate':'before_break'}, inplace = True)
        p2_spin_rates
        
        p2_spin_rates_bar = p2_spin_rates.plot(kind='bar')
        
        st.pyplot()
        
    # Average Velo Bar Charts
    if chart_options == 'Velocity':
        st.write('## Pitcher 2 Average Velocities')
               
        p2_velo = pd.DataFrame(pitcher2b.groupby('pitch_type')['release_velo'].mean())
        p2_velo['after_break'] = pd.DataFrame(pitcher2a.groupby('pitch_type')['release_velo'].mean())
        p2_velo.rename(columns = {'release_velo':'before_break'}, inplace = True)
        p2_velo
        
        p2_velo_bar = p2_velo.plot(kind='bar')
        
        st.pyplot()
    
    # Strike Chart
    if chart_options == 'Pitch Location':
        st.write('## Pitcher 2 Pitch Location')
                 
        # Pitch Location by Handedness of Batter
        handedness = st.selectbox('Righties, Lefties, or both?', ['Righties', 'Lefties', 'Both'])
        
        if handedness == 'Both':
            
            if st.checkbox('P2 Locations Before Break'):
                
                location_chart2b = pitcher2b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                pitcher2b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2b, color='blue', label='Changeup')
                pitcher2b.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2b, color='purple', label='Two-Seam Fastball')
                pitcher2b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2b, color='yellow', label='Slider')
                pitcher2b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2b, color='green', label='Curveball')
                 
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart2b.legend()
                
                location_chart2b.add_patch(rect)
                
                st.pyplot()
            
            if st.checkbox('P2 Locations After Break'):
                
                location_chart2a = pitcher2a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                pitcher2a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2a, color='blue', label='Changeup')
                pitcher2a.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2a, color='purple', label='Two-Seam Fastball')
                pitcher2a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2a, color='yellow', label='Slider')
                pitcher2a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2a, color='green', label='Curveball')
                
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart2a.legend()
                
                location_chart2a.add_patch(rect)
                
                st.pyplot()
                
        if handedness == 'Righties':
            st.write('## Pitcher 2 Pitch Location Against Righties')
            
            if st.checkbox('P2 Location Before Break (R)'):
                righties_p2b = pd.DataFrame(pitcher2b.query('bats=="R"'))
                
                righties_p2b_count = righties_p2b.pitch_type.value_counts()
                
                righties_p2b_count
                
                location_chart2rb = righties_p2b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                righties_p2b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2rb, color='blue', label='Changeup')
                righties_p2b.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2rb, color='purple', label='Two-Seam Fastball')
                righties_p2b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2rb, color='yellow', label='Slider')
                righties_p2b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2rb, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart2rb.legend()
                
                location_chart2rb.add_patch(rect)
                
                st.pyplot()
                
                
                
            if st.checkbox('P2 Location After Break (R)'):
                righties_p2a = pd.DataFrame(pitcher2a.query('bats=="R"'))
                
                righties_p2a_count = righties_p2a.pitch_type.value_counts()
                
                righties_p2a_count
                
                location_chart2ra = righties_p2a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                righties_p2a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2ra, color='blue', label='Changeup')
                righties_p2a.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2ra, color='purple', label='Two-Seam Fastball')
                righties_p2a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2ra, color='yellow', label='Slider')
                righties_p2a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2ra, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart2ra.legend()
                
                location_chart2ra.add_patch(rect)
                
                st.pyplot()
                
        
        if handedness == 'Lefties':   
            st.write('## Pitcher 2 Pitch Selection Against Lefties')
                     
            if st.checkbox('P2 Location Before Break (L)'):
                lefties_p2b = pd.DataFrame(pitcher2b.query('bats=="L"'))
                
                lefties_p2b_count = lefties_p2b.pitch_type.value_counts()
                
                lefties_p2b_count
                
                location_chart2lb = lefties_p2b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                lefties_p2b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2lb, color='blue', label='Changeup')
                lefties_p2b.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2lb, color='purple', label='Two-Seam Fastball')
                lefties_p2b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2lb, color='yellow', label='Slider')
                lefties_p2b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2lb, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart2lb.legend()
                
                location_chart2lb.add_patch(rect)
                
                st.pyplot()
                
            if st.checkbox('P2 Location After Break (L)'):
                lefties_p2a = pd.DataFrame(pitcher2a.query('bats=="L"'))
                
                lefties_p2a_count = lefties_p2a.pitch_type.value_counts()
                
                lefties_p2a_count
                
                location_chart2la = lefties_p2a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                lefties_p2a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2la, color='blue', label='Changeup')
                lefties_p2a.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2la, color='purple', label='Two-Seam Fastball')
                lefties_p2a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2la, color='yellow', label='Slider')
                lefties_p2a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart2la, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart2la.legend()
                
                location_chart2la.add_patch(rect)
                
                st.pyplot()
            
    # Catcher Pie Charts
    if chart_options == 'Catchers':
        st.write('## Pitcher 2 Catchers')
        
        if st.checkbox('P2 Catchers Before Break'):
            p2b_catchers = pitcher2b.catcherid.value_counts()
            p2b_catcher_pie = p2b_catchers.plot(kind='pie', colors=['red', 'blue', 'purple'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p2b_catchers
            
            st.pyplot()
        
        if st.checkbox('P2 Catchers After Break'):
            p2a_catchers = pitcher2a.catcherid.value_counts()
            p2a_catcher_pie = p2a_catchers.plot(kind='pie', colors=['yellow', 'red'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p2a_catchers
        
            st.pyplot()
            
        if st.checkbox('Catcher Strike Percentages'):
            p2_balls = pd.DataFrame(balls.query('pitcherid==2'))
            p2_strikes = pd.DataFrame(strikes.query('pitcherid==2'))
            p2_catchers = pd.DataFrame(p2_balls.groupby('catcherid')['pitch_result'].count())
            p2_catchers['strikes'] = pd.DataFrame(p2_strikes.groupby('catcherid')['pitch_result'].count())
            p2_catchers.rename(columns = {'pitch_result':'balls'}, inplace = True)
            p2_catchers
            
            p2_catcher_framing = p2_catchers.iloc[0].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            
            p2_catcher_framing = p2_catchers.iloc[1].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            
            p2_catcher_framing = p2_catchers.iloc[2].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            
            p2_catcher_framing = p2_catchers.iloc[3].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            

# Pitcher 3
if pitcher_option == 'Pitcher 3':
    
    chart_options = st.selectbox('Which chart would you like to view?', ['Pitch Break Chart', 'Pitch Selection', 'Spin Rate', 'Velocity', 'Pitch Location', 'Catchers'])
    
    # Break Charts
    if chart_options == 'Pitch Break Chart':
        st.write('## Pitcher 3 Break Charts')
                 
        if st.checkbox('P3 Before Break'):        
            break_chart3b = pitcher3b.query('pitch_type=="FF"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), color='red', label='Fastball')
            pitcher3b.query('pitch_type=="CH"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3b, color='blue', label='Changeup')
            pitcher3b.query('pitch_type=="FT"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3b, color='grey', label='Two-Seam Fastball')
            pitcher3b.query('pitch_type=="SL"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3b, color='yellow', label='Slider')
            pitcher3b.query('pitch_type=="CB"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3b, color='green', label='Curveball')
            
            break_chart3b.set_ylabel('Vertical Movement')
            break_chart3b.set_xlabel('Horizontal Movement')
            break_chart3b.legend()
        
            st.pyplot()
            
        if st.checkbox('P3 After Break'):        
            break_chart3a = pitcher3a.query('pitch_type=="FF"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), color='red', label='Fastball')
            pitcher3a.query('pitch_type=="CH"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3a, color='blue', label='Changeup')
            pitcher3a.query('pitch_type=="FT"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3a, color='grey', label='Two-Seam Fastball')
            pitcher3a.query('pitch_type=="SL"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3a, color='yellow', label='Slider')
            pitcher3a.query('pitch_type=="CB"').plot(kind='scatter', x='pfx_x', y = 'pfx_z', xlim=(-30,30), ylim=(-30,30), ax=break_chart3a, color='green', label='Curveball')
            
            break_chart3a.set_ylabel('Vertical Movement')
            break_chart3a.set_xlabel('Horizontal Movement')
            break_chart3a.legend()
        
            st.pyplot()
        
    # Pitch Selection Pie Charts
    if chart_options == 'Pitch Selection':
        st.write('## Pitcher 3 Pitch Selection')
        if st.checkbox('P3 Pitches Before Break'):
            p3b_pitch_counts = pitcher3b.pitch_type.value_counts()
            p3b_pitch_pie = p3b_pitch_counts.plot(kind='pie', colors=['red', 'blue', 'purple', 'yellow', 'green'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p3b_pitch_counts
            
            st.pyplot()
        
        if st.checkbox('P3 Pitches After Break'):
            p3a_pitch_counts = pitcher3a.pitch_type.value_counts()
            p3a_pitch_pie = p3a_pitch_counts.plot(kind='pie', colors=['red', 'blue', 'purple', 'yellow', 'green'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p3a_pitch_counts
            
            st.pyplot()
            
    # Spin Rate Bar Charts
    if chart_options == 'Spin Rate':
        st.write('## Pitcher 3 Spin Rates')
        
        p3_spin_rates = pd.DataFrame(pitcher3b.groupby('pitch_type')['spin_rate'].mean())
        p3_spin_rates['after_break'] = pd.DataFrame(pitcher3a.groupby('pitch_type')['spin_rate'].mean())
        p3_spin_rates.rename(columns = {'spin_rate':'before_break'}, inplace = True)
        p3_spin_rates
        
        p3_spin_rates_bar = p3_spin_rates.plot(kind='bar')
        
        st.pyplot()
        
    # Average Velo Bar Charts
    if chart_options == 'Velocity':
        st.write('## Pitcher 3 Average Velocities')
               
        p3_velo = pd.DataFrame(pitcher3b.groupby('pitch_type')['release_velo'].mean())
        p3_velo['after_break'] = pd.DataFrame(pitcher3a.groupby('pitch_type')['release_velo'].mean())
        p3_velo.rename(columns = {'release_velo':'before_break'}, inplace = True)
        p3_velo
        
        p3_velo_bar = p3_velo.plot(kind='bar')
        
        st.pyplot()

    # Strike Chart
    if chart_options == 'Pitch Location':
        st.write('## Pitcher 3 Pitch Location')
        
        # Pitch Location by Handedness of Batter
        handedness = st.selectbox('Righties, Lefties, or both?', ['Righties', 'Lefties', 'Both'])
        
        if handedness == 'Both':
        
            if st.checkbox('P3 Locations Before Break'):
                
                location_chart3b = pitcher3b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                pitcher3b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3b, color='blue', label='Changeup')
                pitcher3b.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3b, color='purple', label='Two-Seam Fastball')
                pitcher3b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3b, color='yellow', label='Slider')
                pitcher3b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3b, color='green', label='Curveball')
                
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart3b.legend()
                
                location_chart3b.add_patch(rect)
                
                st.pyplot()
            
            if st.checkbox('P3 Locations After Break'):
                
                location_chart3a = pitcher3a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                pitcher3a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3a, color='blue', label='Changeup')
                pitcher3a.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3a, color='purple', label='Two-Seam Fastball')
                pitcher3a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3a, color='yellow', label='Slider')
                pitcher3a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3a, color='green', label='Curveball')
                
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart3a.legend()
                
                location_chart3a.add_patch(rect)
                
                st.pyplot()
                
        if handedness == 'Righties':
            st.write('## Pitcher 3 Pitch Location Against Righties')
            
            if st.checkbox('P3 Location Before Break (R)'):
                righties_p3b = pd.DataFrame(pitcher3b.query('bats=="R"'))
                
                righties_p3b_count = righties_p3b.pitch_type.value_counts()
                
                righties_p3b_count
                
                location_chart3rb = righties_p3b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                righties_p3b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3rb, color='blue', label='Changeup')
                righties_p3b.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3rb, color='purple', label='Two-Seam Fastball')
                righties_p3b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3rb, color='yellow', label='Slider')
                righties_p3b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3rb, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart3rb.legend()
                
                location_chart3rb.add_patch(rect)
                
                st.pyplot()

                
            if st.checkbox('P3 Location After Break (R)'):
                righties_p3a = pd.DataFrame(pitcher3a.query('bats=="R"'))
                
                righties_p3a_count = righties_p3a.pitch_type.value_counts()
                
                righties_p3a_count
                
                location_chart3ra = righties_p3a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                righties_p3a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3ra, color='blue', label='Changeup')
                righties_p3a.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3ra, color='purple', label='Two-Seam Fastball')
                righties_p3a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3ra, color='yellow', label='Slider')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart3ra.legend()
                
                location_chart3ra.add_patch(rect)
                
                st.pyplot()
                
        
        if handedness == 'Lefties':   
            st.write('## Pitcher 3 Pitch Selection Against Lefties')
                     
            if st.checkbox('P3 Location Before Break (L)'):
                lefties_p3b = pd.DataFrame(pitcher3b.query('bats=="L"'))
                
                lefties_p3b_count = lefties_p3b.pitch_type.value_counts()
                
                lefties_p3b_count
                
                location_chart3lb = lefties_p3b.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                lefties_p3b.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3lb, color='blue', label='Changeup')
                lefties_p3b.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3lb, color='purple', label='Two-Seam Fastball')
                lefties_p3b.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3lb, color='yellow', label='Slider')
                lefties_p3b.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3lb, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart3lb.legend()
                
                location_chart3lb.add_patch(rect)
                
                st.pyplot()
                
            if st.checkbox('P3 Location After Break (L)'):
                lefties_p3a = pd.DataFrame(pitcher3a.query('bats=="L"'))
                
                lefties_p3a_count = lefties_p3a.pitch_type.value_counts()
                
                lefties_p3a_count
                
                location_chart3la = lefties_p3a.query('pitch_type=="FF"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), color='red', label='Fastball')
                lefties_p3a.query('pitch_type=="CH"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3la, color='blue', label='Changeup')
                lefties_p3a.query('pitch_type=="FT"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3la, color='purple', label='Two-Seam Fastball')
                lefties_p3a.query('pitch_type=="SL"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3la, color='yellow', label='Slider')
                lefties_p3a.query('pitch_type=="CB"').plot(kind='scatter', x='x', y = 'z', xlim=(-40,35), ylim=(-20,75), ax=location_chart3la, color='green', label='Curveball')
            
                # Create a Rectangle patch
                rect = Rectangle((-10,10),20,30,linewidth=3,edgecolor='black',facecolor='none')
                
                location_chart3la.legend()
                
                location_chart3la.add_patch(rect)
                
                st.pyplot()
        
    # Catcher Pie Charts
    if chart_options == 'Catchers':
        st.write('## Pitcher 3 Catchers')
        
        if st.checkbox('P3 Catchers Before Break'):
            p3b_catchers = pitcher3b.catcherid.value_counts()
            p3b_catcher_pie = p3b_catchers.plot(kind='pie', colors=['red', 'blue', 'purple', 'yellow'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p3b_catchers
            
            st.pyplot()
        
        if st.checkbox('P3 Catchers After Break'):
            p3a_catchers = pitcher3a.catcherid.value_counts()
            p3a_catcher_pie = p3a_catchers.plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7))
            p3a_catchers
        
            st.pyplot()
            
        if st.checkbox('Catcher Strike Percentages'):
            p3_balls = pd.DataFrame(balls.query('pitcherid==3'))
            p3_strikes = pd.DataFrame(strikes.query('pitcherid==3'))
            p3_catchers = pd.DataFrame(p3_balls.groupby('catcherid')['pitch_result'].count())
            p3_catchers['strikes'] = pd.DataFrame(p3_strikes.groupby('catcherid')['pitch_result'].count())
            p3_catchers.rename(columns = {'pitch_result':'balls'}, inplace = True)
            p3_catchers
            
            p3_catcher_framing = p3_catchers.iloc[0].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            
            p3_catcher_framing = p3_catchers.iloc[1].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()
            
            p3_catcher_framing = p3_catchers.iloc[3].plot(kind='pie', colors=['red', 'blue'], autopct='%.2f', fontsize=19, figsize=(7, 7), subplots=True)
            st.pyplot()