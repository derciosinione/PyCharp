using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;

namespace frontend
{
    public partial class Form1 : Form
    {
        ops.Userqueries query = new ops.Userqueries();
        public Form1()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            try
            {
                    using (HttpClient client = new HttpClient())
                    {
                        var value = new Dictionary<string, string> { { "query", query.allNetworkcredentials }, };
                        var contentQuery = new FormUrlEncodedContent(value);

                        using (HttpResponseMessage res = await client.PostAsync(ops.config.baseUrl, contentQuery))
                        {
                            using (HttpContent content = res.Content)
                            {
                                string data = await content.ReadAsStringAsync();

                                MessageBox.Show(data);
                                listBox1.Items.Clear();
                                listBox1.Items.Add(data);
                            }
                        }
                    }
            }
            catch (Exception ms)
            {
                MessageBox.Show(ms.Message);
            }
        }
    }
}
