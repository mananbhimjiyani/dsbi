from flask import render_template, Blueprint
from flask_login import login_required, current_user
from flask import request, redirect, url_for
from app.utils import predict_ctr
from app.models import AdCampaign
from app import db


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('base.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    campaigns = AdCampaign.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', campaigns=campaigns)


@main_bp.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method == 'POST':
        form_data = {
            'campaign_id': request.form['campaign_id'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'interest1': request.form['interest1'],
            'interest2': request.form['interest2'],
            'interest3': request.form['interest3'],
            'impressions': request.form['impressions'],
            'clicks': request.form['clicks'],
            'spent': request.form['spent'],
            'total_conversion': request.form['total_conversion'],
            'approved_conversion': request.form['approved_conversion'],
        }
        predicted_ctr = predict_ctr(form_data)
        # Save to DB
        campaign = AdCampaign(**form_data, predicted_ctr=predicted_ctr, user_id=current_user.id)
        db.session.add(campaign)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('predict.html')

